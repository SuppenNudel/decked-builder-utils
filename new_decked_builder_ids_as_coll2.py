import os

exec_dir = os.path.dirname(os.path.realpath(__file__))
target_file = exec_dir+'/wrong_ids.coll2'


def main():
    f = open(target_file, 'w')
    f.writelines('doc:\n')
    f.writelines('- version: 1\n')
    f.writelines('- items:\n')
    for id in range(1234567, 1250000):
        print(id)
        f.writelines(f'  - - id: {id}\n')
        f.writelines('    - r: 1\n')


if __name__ == '__main__':
    main()
