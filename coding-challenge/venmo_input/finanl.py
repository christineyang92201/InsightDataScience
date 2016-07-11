import re
import networkx as nx
import matplotlib.pyplot as plt


def reGraph(reDict,nameDict,count):
    #print nameDict
    "draw graph"
    reNodes = []
    reValues = []
    reEdges = []

    for key in reDict:
        reEdges.append(key)

    for keyName in nameDict:
        #print keyName
        #print nameDict[keyName]
        reNodes.append(keyName)
        #print nameDict
        reValues.append(nameDict[keyName])

    g = nx.Graph()
    g.add_nodes_from(reNodes)
    g.add_nodes_from(reEdges)

    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g,pos,nodelist=reNodes, node_color='w', node_size=1000)
    nx.draw_networkx_edges(g,pos,edgelist=reEdges,edge_color='b')
    labelsName = {}
    labelsValue = {}
    for i in range(len(reNodes)):
        labelsName[reNodes[i]] = reNodes[i]
        labelsValue[reNodes[i]] = reValues[i]


    nx.draw_networkx_labels(g,pos,labelsName,font_size=16)
    plt.savefig('./exampleGraph/Name' + str(count) + '.png')
    plt.show()
    plt.close()

def midnum(inputDict):
    val = []
    for k in inputDict:
        val.append(inputDict[k])

    sval = sorted(val)
    #print sval
    if len(val) %2==1:
        res = sval[(len(val)-1)/2]
    else:
        res = (sval[len(val)/2]+sval[(len(val)/2-1)])/2.0
    res = "{:.2f}".format(res)
    #print res
    return res




def reGraphvalue(reDict,nameDict,count):
    print nameDict
    "draw graph"
    reNodes = []
    reValues = []
    reEdges = []

    for key in reDict:
        reEdges.append(key)

    for keyName in nameDict:
        #print keyName
        #print nameDict[keyName]
        reNodes.append(keyName)
        #print nameDict
        reValues.append(nameDict[keyName])

    g = nx.Graph()
    g.add_nodes_from(reNodes)
    g.add_nodes_from(reEdges)

    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g,pos,nodelist=reNodes, node_color='w', node_size=1000)
    nx.draw_networkx_edges(g,pos,edgelist=reEdges,edge_color='b')
    labelsName = {}
    labelsValue = {}
    for i in range(len(reNodes)):
        labelsName[reNodes[i]] = reNodes[i]
        labelsValue[reNodes[i]] = reValues[i]


    nx.draw_networkx_labels(g,pos,labelsValue,font_size=16)
    plt.savefig('./exampleGraph/Value' + str(count) + '.png')
    plt.show()
    plt.close()
















def timeTransform(time):
    time = time.translate(None,"Z")
    yearMonDayTimels = time.split("T")
    yearMonDay = yearMonDayTimels[0].split("-")
    Day = int(yearMonDay[2])
    #print Day
    timestr = yearMonDayTimels[1]
    timels = timestr.split(":")
    hour = int(timels[0])
    min = int(timels[1])
    seconds = int(timels[2])

    timetrans = Day*24*3600 + hour*3600 + min*60 + seconds
    return timetrans

def tuToList_keys(inputkeys):
    keylens = len(inputkeys)
    keylist = []
    for i in range(keylens):
        thiskeys = list(inputkeys[i])
        keylist.append(thiskeys)

    return keylist




def reForNow(inputDict):
    res = {}
    for thisnum in inputDict:
        thisRecord = inputDict[thisnum]
        # print thisRecord
        lenRecord = len(thisRecord)
        # if lenRecord == 1:
        #     target = thisRecord[]
        #     res[target,actor] = thisnum
        # else:
        for i in range(lenRecord):
            recordNow = thisRecord[i]
            target = recordNow[0]
            actor = recordNow[1]
            res[target,actor] = thisnum
    return res

def rePosition(inputDict,imkey, tg, act):
    "tg and actor are imported as string for target and actor"
    "This function used to delete a record"
    thisrecord = inputDict[imkey]
    #print thisrecord
    if len(thisrecord) == 1:
        del inputDict[imkey]
    else:
        for i in range(len(thisrecord)):
            #print i

            if tg in thisrecord[i] and act in thisrecord[i]:
                inputDict[imkey].remove(thisrecord[i])
                break
            else:
                continue
    res = inputDict
    return res









def main():
    plt.close("all")
    inFile = open("example.txt","r")
    outFile = open("output.txt","w")
    outFile.write('Median Degree')
    outFile.write('\n')
    lines = inFile.readlines()
    #print lines
    #lines = lines[]
    # print lines

    count = 0
    uselesscount = 0
    timeName = {}
    valueName = {}
    maxtime = 0
    md = []


    for line in lines:
        #print line
        count = count +1
        outFile.write("*********************************\n")
        outFile.write(str(count-uselesscount) + "th useful data arrives:")
        outFile.write("\n")
        outFile.write(line)

        #line = line.translate(None,"\n")
        #print line
        #print "\n"
        lineCell = re.findall(r"['\"](.*?)['\"]", line)
        #print lineCell

        target = lineCell[3]
        if target == '':
            print "Ignore this record, since there is no value for target.\n"
            print line
            print "***************************"
            uselesscount = uselesscount +1
            continue

        actor = lineCell[5]
        if actor == '':
            print "Ignore this record, since there is no value for actor.\n"
            print line
            print "***************************"
            uselesscount = uselesscount +1
            continue

        time = lineCell[1].strip()
        timeSeconds = timeTransform(time)
        target = target.strip()
        actor = actor.strip()

        "check if all records are on the same date"

        "Update new useful information for graph"

        "Identify if a record is out of order"
        "time function"
        if  (count-uselesscount) == 1:
            "first record - Initilization"
            timeName[timeSeconds] = [[target, actor, time]]
            valueName[target] = 1
            valueName[actor] = 1
            maxtime = timeSeconds
        else:
            #print lineCell
            #print type(lineCell)
            #print time
            #print target
            #print actor
            "convert keys in tuple to all keys in a list"
            listkeys = tuToList_keys(relatn.keys())
            #print listkeys
            #print [target,actor]
            #print 'target is ' + target
            #print 'actor is ' + actor
            #print [actor,target]
            #print listkeys[0]



            if [target,actor] in listkeys or [actor,target] in listkeys:
                #print 'target is ' + target
                #print 'actor is ' + actor
                #print listkeys


                if [target,actor] in listkeys:
                    #print relatn
                    thisoldtime = relatn[(target,actor)]
                    if timeSeconds < thisoldtime:
                        md.append(md[len(md)-1])
                        outFile.write("The median degree list is")
                        outFile.write("\n")
                        outFile.write(str(md))
                        outFile.write("\n")

                        continue
                    else:
                        "delete the old record"
                        timeName = rePosition(timeName, thisoldtime, target, actor)
                        valueName[target] = valueName[target] - 1
                        valueName[actor] = valueName[actor] - 1
                    # print thisoldtime
                else:
                    transtarget = target
                    target = actor
                    actor = transtarget
                    thisoldtime = relatn[(target,actor)]
                    if timeSeconds < thisoldtime:
                        md.append(md[len(md) - 1])
                        outFile.write("The median degree list is")
                        outFile.write("\n")
                        outFile.write(str(md))
                        outFile.write("\n")

                        continue
                    else:
                        "delete the old record"

                        timeName = rePosition(timeName, thisoldtime, target, actor)
                        valueName[target] = valueName[target] - 1
                        valueName[actor] = valueName[actor] - 1




            #print timeName
            #print valueName

            if timeSeconds < maxtime:
                "out of order"
                if maxtime - timeSeconds < 60:
                    "within 60 seconds"

                    "Update valueName dictionary"
                    if target in valueName.keys():
                        #print "run ?"
                        valueName[target] = valueName[target] +1
                    else:
                        valueName[target] = 1
                    if actor in valueName.keys():
                        valueName[actor] = valueName[actor] +1
                    else:
                        valueName[actor] = 1
                    "Update timeName dictionary which contains all useful information"
                    if timeSeconds in timeName.keys():
                        timeName[timeSeconds].append([target, actor, time])
                    else:
                        timeName[timeSeconds] = [[target, actor, time]]
                else:
                    "out of 60 seconds"
                    #print "This record " + str(count) + " is out of order and exceed 60 seconds of the maximum time"
                    # print timeName
                    # print valueName
                    #print "The maximum time for now is " + timeName[maxtime][0][2]
                    #print "***************************"
                    md.append(md[len(md) - 1])
                    outFile.write("The median degree list is")
                    outFile.write("\n")
                    outFile.write(str(md))
                    outFile.write("\n")

                    continue
            else:
                "in order"
                maxtime = timeSeconds

                for oldtime in timeName.keys():
                    # print "run?"
                    if maxtime - oldtime <60:

                        continue
                    else:
                        recordrming = timeName[oldtime]
                        # print recordrming
                        length = len(recordrming)
                        for i in range(length):
                            targetrm = recordrming[i][0]
                            # print targetrm
                            actorrm = recordrming[i][1]
                            # print actorrm
                            valueName[targetrm] = valueName[targetrm] -1
                            valueName[actorrm] = valueName[actorrm] -1
                        for thisName in valueName.keys():
                            if valueName[thisName] == 0:
                                del valueName[thisName]
                            else:
                                continue


                        del timeName[oldtime]
                "update valueName"
                if target in valueName:
                    valueName[target] = valueName[target] + 1
                else:
                    valueName[target] = 1
                if actor in valueName:
                    valueName[actor] = valueName[actor] + 1
                else:
                    valueName[actor] = 1
                "update timeName"
                if timeSeconds in timeName:
                    timeName[timeSeconds].append([target,actor,time])
                else:
                    timeName[timeSeconds] = [[target,actor,time]]



        #print timeName
        #print valueName

        relatn = reForNow(timeName)
        #print relatn

        #count = count +1

        #reGraph(relatn, valueName, count-1)
        #reGraphvalue(relatn,valueName,count-1)
        mdvalue = midnum(valueName)
        md.append(mdvalue)
        #print "The median degree list is "
        #print '\n'
        #print str(md)
        outFile.write("The median degree list is")
        outFile.write("\n")
        outFile.write(str(md))
        outFile.write("\n")
        # for i in range(len(md)):
        #    print str(md[i])
        #    print '\n'

        #print "The maximum time for now is " + timeName[maxtime][0][2]

        #print "***************************"
    outFile.close()




if __name__ == '__main__':
    main()

