from src.actions.getWorker import getWorkerss

allWorkersID = []
def AllWorkersTgID() :
    getAllWorkers = getWorkerss()
    for j in range(len(getAllWorkers)) :
        if getAllWorkers[j]['tg_id'] != 0 :
            allWorkersID.append(getAllWorkers[j]['tg_id'])
    
    return allWorkersID