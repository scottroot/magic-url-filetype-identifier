import os

def set_env_vars(var_dict):
    for key in list(var_dict.keys()):
        os.environ.setdefault(key, var_dict[key])
environment_variables = {
    # TIKA_VERSION - set to the version string, e.g., 1.12
    'TIKA_VERSION': '1.9',
    # TIKA_SERVER_JAR - full URL to the remote Tika server jar to download
    'TIKA_SERVER_JAR': 'file:////tika-server-1.9.jar',
    # TIKA_SERVER_ENDPOINT - set to the host (local or remote)
    'TIKA_SERVER_ENDPOINT': 'localhost',
    # TIKA_CLIENT_ONLY - if set to True: then TIKA_SERVER_JAR is ignored: 
    # and relies on the value for TIKA_SERVER_ENDPOINT and treats Tika like a REST client.
    'TIKA_CLIENT_ONLY': 'false',
    # TIKA_TRANSLATOR - set to the fully qualified class name (defaults to Lingo24 for the Tika translator implementation.
    'TIKA_SERVER_JAR': 'file:////tika-server.jar',
    # TIKA_SERVER_CLASSPATH - set to a string (delimited by ':' for each additional path to prepend to the Tika server jar path.
    'TIKA_SERVER_JAR': 'file:////tika-server.jar',
    # TIKA_LOG_PATH - set to a directory with write permissions and the tika.log and tika-server.log files will be placed in this directory.
    'TIKA_SERVER_JAR': 'file:////tika-server.jar',
    # TIKA_PATH - set to a directory with write permissions and the tika_server.jar file will be placed in this directory.
    'TIKA_SERVER_JAR': 'file:////tika-server.jar',
    # TIKA_JAVA - set the Java runtime name: e.g.: java or java9
    'TIKA_JAVA': 'java',
    # TIKA_STARTUP_SLEEP - number of seconds (float to wait per check if Tika server is launched at runtime
    'TIKA_SERVER_JAR': 'file:////tika-server.jar',
    # TIKA_STARTUP_MAX_RETRY - number of checks (int to attempt for Tika server startup if launched at runtime
    'TIKA_SERVER_JAR': 'file:////tika-server.jar',
    # TIKA_JAVA_ARGS - set java runtime arguments: e.g: -Xmx4g
    'TIKA_SERVER_JAR': 'file:////tika-server.jar',
    # TIKA_LOG_FILE - set the filename for the log file. default: tika.log. if it is an empty string ('': no log file is created.
    'TIKA_SERVER_JAR': 'file:////tika-server.jar'
    }





# Checking the value of the environment variable
if os.environ.get('DEBUG') == 'True':
    print('Debug mode is on')
else:
    print('Debug mode is off')
