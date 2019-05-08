from . import dists
import csv

class Searcher:

    def __init__(self,dbPath):

        self.dbPath = dbPath
        #print(dbPath)

    def search(self,queryFeatures,numResults=10):

        results ={}

        with open(self.dbPath) as f:
            reader = csv.reader(f)
            for row in reader:
                features = [float(x) for x in row[1:]]
                d = dists.chi2_distance(features, queryFeatures)
                results[row[0]] = d
            f.close()
        # sort our results, so that the smaller distances (i.e. the more relevant images)
        # are at the front of the list)
        results = sorted([(v, k) for (k, v) in results.items()])

        return results[:numResults]
    


