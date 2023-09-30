export function get_color_css_variables(color, shades = []) {
    if (color === null) {
        return null;
    }

    let variables = [];

    if (typeof color == String) {
        shades.forEach(shade => {
            variables.push(`--c-${shade}:var(--${color}-${shade})`)
        });
    }

    if (typeof color == Array) {
        shades.forEach(shade => {
            variables.push(`--c-${shade}:${color[shade]}`)
        });
    }

    return variables.join(';');
}