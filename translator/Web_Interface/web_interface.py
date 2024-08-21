'''
Web interface that mirrors the command line application.
Note this has been made for Mac, and may not work with other operating systems.

Run python3 web_interface.py from command line to run, and then open http://127.0.0.1:8080/ on a local browser.
'''



from flask import Flask, request, render_template
import threading
from ..Equivalence_Applier.filter import filter_equivalences
from ..Equivalence_Applier.applier import apply_equivalences
from ..command_line import check_dependencies, parse_command
import os

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    
    base_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Set the template and static folder paths
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    
    print(f"Base directory: {base_dir}")
    print(f"Template directory: {template_dir}")
    print(f"Static directory: {static_dir}")
    
    @app.route('/', methods=['GET', 'POST'])

    def index():
        """
        Handle the main page of the web interface.
        - GET: Renders the input form.
        - POST: Processes the form data, applies logical equivalences, and returns the results.

        Returns:
            - The rendered HTML template with error messages or results if applicable.
        """
        
        if request.method == 'POST':
            # Construct a command string from the form inputs
            raw_command = f'transform "{request.form.get("formula")}" {request.form.get("operators")} {request.form.get("complexity")} {request.form.get("depth")} {request.form.get("show_unfiltered")} {request.form.get("timeout")}'
            
            try:
                # Parse the command string using the command-line parsing function
                formula, operators, complexity, depth, show_unfiltered, timeout = parse_command(raw_command)
            except ValueError as e:
                # Render the form with an error message if parsing fails
                return render_template('index.html', error=f"Error: {str(e)}")

            # Check for unreachable operators based on the selected operators
            unreachable = check_dependencies(operators)
            warning_message = None
            if unreachable:
                warning_message = f"Warning: The following operators might not always be reachable: {', '.join(unreachable)}."

            # Prepare to store the result or any exception that might occur
            result = []
            exception = []

            def run_apply_equivalences():
                """
                Run the equivalence application function in a separate thread.
                Stores the result in the 'result' list or any exception in the 'exception' list.
                """
                try:
                    result.append(apply_equivalences(formula, complexity, depth))
                except Exception as e:
                    exception.append(e)

            # Run the equivalence application in a separate thread with a timeout
            thread = threading.Thread(target=run_apply_equivalences)
            thread.start()
            thread.join(timeout)

            if thread.is_alive():
                # Render the form with a timeout error if the operation takes too long
                return render_template('index.html', error=f"Timeout: Equivalence generation took longer than {timeout} seconds.", warning=warning_message)

            if exception:
                # Render the form with an error message if an exception occurred
                return render_template('index.html', error=f"An error occurred: {exception[0]}", warning=warning_message)

            equivalents = result[0]

            if show_unfiltered:
                # Show unfiltered results if requested
                unfiltered_results = [eq._str() for eq in equivalents]
            else:
                unfiltered_results = None

            # Filter the equivalences based on the selected operators
            filtered_equivalents = filter_equivalences(equivalents, operators)

            if len(filtered_equivalents) == 0:
                # Render the form with a message if no results are found after filtering
                return render_template('index.html', error="No equivalent statements generated after filtering.", warning=warning_message, unfiltered=unfiltered_results)
            
            # Render the form with the filtered and unfiltered results
            filtered_results = [eq._str() for eq in filtered_equivalents]
            return render_template('index.html', filtered=filtered_results, unfiltered=unfiltered_results, warning=warning_message)

        # Render the form for GET requests
        return render_template('index.html')

    return app

def run_web_interface():
    '''
    Runs the web interface application.

    This function creates the Flask app and runs it on localhost
    with debugging enabled. It's designed to be called from the
    command line or as an entry point.
    '''
    app = create_app()
    print(f"Template folder: {app.template_folder}")  # Debug print
    app.run(host='127.0.0.1', port=8080, debug=True)

if __name__ == '__main__':
    run_web_interface()