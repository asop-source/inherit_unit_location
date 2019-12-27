
def get_default_unit(odoo, user, _logger):
    employee = odoo.env['hr.employee'].search([('user_id', '=', user.id)])
    if not employee:
        _logger.error('No Employee linked to user %s!' % user.name)
        unit = False
    else:
        if not employee.department_id:
            _logger.error('No Department for Employee %s!' % employee.name)
        unit = employee.department_id.id  # department

    return unit

def get_default_location(odoo, user, _logger):
    employee = odoo.env['hr.employee'].search([('user_id', '=', user.id)])
    if not employee:
        _logger.error('No Employee linked to user %s!' % user.name)
        location=False
    else:
        if not employee.work_location:
            _logger.error('No Work Location for Employee %s!' % employee.name)
        location = employee.work_location.id  # analytic tag
    return location