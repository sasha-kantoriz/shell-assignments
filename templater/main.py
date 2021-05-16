import sys
import yaml
import jinja2
from collections import OrderedDict

def main():
    def arabic2roman(integer):
        integer = int(integer)
        d_int_roman = OrderedDict()

        d_int_roman[1000] = "M"
        d_int_roman[900] = "CM"
        d_int_roman[500] = "D"
        d_int_roman[400] = "CD"
        d_int_roman[100] = "C"
        d_int_roman[90] = "XC"
        d_int_roman[50] = "L"
        d_int_roman[40] = "XL"
        d_int_roman[10] = "X"
        d_int_roman[9] = "IX"
        d_int_roman[5] = "V"
        d_int_roman[4] = "IV"
        d_int_roman[1] = "I"
        """Convert Integer to Roman numeral."""
        roman_list = []
        # Handle conversion rules detailed in specification
        # while iterating over conversion ordered dictionary
        for key in d_int_roman:
            if key > integer:
                continue  # Restart loop until input int <= key
            q = integer // key  # // instead of divmod, remainder unused
            if not q:
                continue
            roman_list.append(d_int_roman[key] * q)
            integer -= (key * q)
            if not integer:
                break
        return ''.join(roman_list)
    env = jinja2.Environment(autoescape=True)
    env.filters['arabic2roman'] = arabic2roman
    for f in sys.argv[1:]:
        body = open(f).read().lstrip().split('\n')
        yaml_vars = []
        for i in body:
            if not ':' in i:
                break
            yaml_vars.append(i)
        variables = yaml.load('\n'.join(yaml_vars), yaml.Loader)
        content = '\n'.join(body[body.index(yaml_vars[-1])+1:])
        tm = env.from_string(content)
        print(tm.render(variables))

if __name__ == '__main__':
    main()