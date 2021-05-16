import sys
import tap.parser
import pprint as pp

def main():
    summary = {'summary': []}
    for fname in sys.argv[1:]:
        fresults = {
            'filename': fname,
            'passed': 0,
            'failed': 0,
            'skipped':0
        }
        try:
            parser = tap.parser.Parser()
            for line in parser.parse_file(fname):
                if line.get('_ok') is True: fresults['passed'] += 1
                elif line.get('_ok') is False: fresults['failed'] += 1
                elif '_ok' in line and line.get('_ok') is None: fresults['skipped'] += 1
        except:
            pass
        finally:
            summary['summary'].append(fresults)
    pp.pprint(summary)

if __name__ == '__main__':
    main()