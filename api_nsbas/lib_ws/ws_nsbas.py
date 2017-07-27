# Module (bibliotheque/library) specifique de l'API NSBAS lib_ws_nsbas.py
# Voir a importer ici les bibliotheques necessaires.
# Inclure eventuellement ici :
# Pour chaque webservice, une fonction realisant le coeur du Execute
# Pour chaque webservice, une fonction realisant le coeur du GetResult
import re

# Observons l'etat de progression d'un job
def getJobStatus(id_du_job,jeton_du_processus, ws_status):
# Version a perfectionner (!)
    #{"errorMessage": "", "returnCode": "256", "oarStatus": "Terminated"}
    # Avancement en pourcentage
    percentDone = 50
    terminated = False
    # Accepted / Terminated
    status = ws_status
    retcode = ""

    m = re.search('"returnCode" *: *"(\d+)"', ws_status)
    if m:
        retcode = m.groups()[0]

    m = re.search('oarStatus.*:.*"(.*)"', ws_status)
    if m:
        status = m.groups()[0]
 
    jobStatus = {
        "StatusInfo": {
		"JobID": id_du_job,
        "processToken" : jeton_du_processus,
		"Status":  status,
        "Retcode" : retcode,
		"Progress": percentDone
		}
	}
    return jobStatus


