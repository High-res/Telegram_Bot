from src.actions.getWorker import getWorkerss


tg_id = []
def getWorkerTgID() :
    allWorkers = getWorkerss()
    for w in range(0, len(allWorkers)) :
        if allWorkers[w]['tg_id'] != 0 :
            tg_id.append(allWorkers[w]['tg_id'])
    return tg_id

print(getWorkerTgID())