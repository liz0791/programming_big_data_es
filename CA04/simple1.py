#Elisandra Silva - 10347211

import csv

def read_file(changes):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open('change.txt', 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[0]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits    
    
#parsing and gathering relevant information for further analysis  
def get_info(commits):
    csv_file = []
    dates = []
    times = []
    for i in range(0, 422):
        date_ = commits[i]['date'].split(' ') 
        dates.append(date_[0])
        times.append(date_[1])
        info = [commits[i]['revision'], commits[i]['author'], dates[i], times[i], commits[i]['number_of_lines']]
        csv_file.append(info)
    return csv_file          
            

if __name__ == '__main__':
    # open the file - and read all of the lines.
    change = "change.txt"
    data = read_file(change)
    commits = get_commits(data)
    
    #calling function get_info t create our csv_file in a list   
    csv_file = get_info(commits)
    print (csv_file)
      
        
    #exporting our data as csv 
    with open("output.csv", 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['REVISION', 'AUTHOR', 'DATE', 'TIME', 'NUMBER OF LINES'])
        for row in csv_file:
            spamwriter.writerow(row)
                     
    
