# This is a temporary file to test babs-init


from babs.core_functions import babs_init
import sys
import os
import os.path as op

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "babs"))

flag_where = "cubic"   # "cubic" or "local"
if flag_where == "cubic":
    where_project = "/cbica/projects/BABS/data"
elif flag_where == "local":
    where_project = "/Users/chenyzh/Desktop/Research/Satterthwaite_Lab/datalad_wrapper/data"
else:
    raise Exception("not valid `flag_where`!")

input_ds_name = "fmriprep"
# input_ds = op.join(where_project, "j854e")
# type_session = "multi-ses"
# input_ds = op.join(where_project, "zd9a6")
# type_session = "single-ses"
input_ds = op.join(where_project, "testdata_NKI/fmriprep_multises_outputs")
type_session = "multi-ses"

project_name = "test_babs_" + type_session
bidsapp = "xcpd"
if flag_where == "cubic":
    container_ds = op.join(where_project, "toybidsapp-container")
elif flag_where == "local":
    container_ds = op.join(where_project, "toybidsapp-container-docker")
container_name = bidsapp + "-0-0-0"  # "toybidsapp-0-0-3"
container_config_yaml_file = "example_container_" + bidsapp + ".yaml"

if os.getenv("TEMPLATEFLOW_HOME") is None:
    os.environ['TEMPLATEFLOW_HOME'] = '/templateflow_home_test'

babs_init(where_project, project_name,
          input=[[input_ds_name, input_ds]],
          container_ds=container_ds,
          container_name=container_name,
          container_config_yaml_file=container_config_yaml_file,
          type_session=type_session,
          system="sge")

print("")
