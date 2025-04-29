def insert(intervals, newInterval):
        """
        returns list of intervals, with newInterval inserted

        Keyword arguments:
        intervals a list of intervals sorted by the start of the intervals
        newInterval a list of a new interval to be inserted
        """
        #Initialize the updated intervals list and a boolean reference to know when the new Interval is inserted
        updatedIntervals=[]
        inserted=False
        #Iterate over the intervals list, appending its inverals to the updated list ultil the place for the insert is found
        for i in range(len(intervals)):
            if inserted or intervals[i][1]<newInterval[0]: #Before the place of the insert for the interval is found or once the insert is done, the values will simply be appended
                updatedIntervals.append(intervals[i])
            else: #once the location of the new interval is found, it will be modified with the overlaping existing intervals to create a new one and ensuring no further overlaping is created
                if newInterval[1]<intervals[i][0]: #The final placement for the new interval is found if its last value is less than the first one for the next interval, meaning there is no overlaping
                    updatedIntervals.append(newInterval)
                    updatedIntervals.append(intervals[i])
                    inserted=True
                else: #Else there is overlaping and the new interval is updated acordingly
                    newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        if not inserted: #after the loops, if the interval was not inserted, it will be place at the end
            updatedIntervals.append(newInterval)
        return updatedIntervals

#Example test
if __name__ == "__main__":
  print('Insert Intervals test. intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
  print('Returns: ', insert( [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
