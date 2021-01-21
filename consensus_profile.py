from collections import defaultdict, Counter
import csv


def text_preprocess(filepath='genefiles/rosalind_cons.txt'):
    import re
    pat = re.compile('>(\w+_\d{4})')

    seq_data = []
    with open(filepath, mode='r') as file:
        line_data = []
        for line in file:
            line = line.strip()
            line_data.append(line)

        # replacing pattern with spaces and spliting into lists
        subs = re.sub(pat,  ' ', ''.join(line_data))
        subs = subs.split()
        for seqs in subs:
            data = []
            for seq in seqs.strip():
                data.append(seq)
            seq_data.append(data)
    return seq_data


def consensus_profiling():
    profile_list = defaultdict(list)
    consensus = []

    seq_data = text_preprocess()
    n_rows = len(seq_data[0])
    n_cols = len(seq_data)

    for i in range(n_rows):
        cols = ''
        for j in range(n_cols):
            cols += seq_data[j][i] # get cols 
        profiles = Counter(cols)
        res = sorted(profiles.items(), key=lambda x: x[1], reverse=True)[0] # sorts in reverse order and gets the tuple
        consensus.append(res[0]) # takes the base in the list above
        for base in ['A', 'G', 'C', 'T']:
            val = profiles.get(base, 0)
            profile_list[base].append(val)    
    return consensus, profile_list
            

def main():
    file = open('outputs/rosalind_cons.txt', mode='w')
    csv_writer = csv.writer(file, delimiter=' ')
    consensus, profile_list = consensus_profiling()
    consensus = ''.join(consensus)
    csv_writer.writerow([consensus])
    for key, val in sorted(profile_list.items(), reverse=False):
        val = ' '.join([str(x) for x in val])
        csv_writer.writerow([key + ': ' + val])
    file.close()

if __name__ == '__main__':
    main()
