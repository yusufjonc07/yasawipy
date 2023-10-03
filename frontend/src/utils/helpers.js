export function get_color_css_variables(color, shades = []) {
    
    if (color === null) {
        return null;
    }

    let variables = {};

    if (typeof color == 'string') {
      
        shades.forEach(shade => {
            variables[`--c-${shade}`] = `var(--${color}-${shade})`
        });
    }

    return variables;
}


export function getIcon(name){
    let str_arr = name.split("-")
    let cons = []
    this.icon.split('-').shift().forEach((element) => {
      cons.push(this.capitalized(element))
    })
    return this.$icon[str_arr[0] == 'o' ? 'outline' : 'solid'][cons.join('') + 'Icon']
}
    