def value(val):
    if isinstance(val, (bool, int)):
        return str(val).lower()
    elif isinstance(val, list):
        return ','.join(val)
    else:
        return val


def key(k):
    match k:
        case 'ids':
            return 'ids'
        case 'keys':
            return 'keys'
        case 'space_type':
            return 'type'
        case 'status':
            return 'status'
        case 'labels':
            return 'labels'
        case 'favorited_by':
            return 'favorited-by'
        case 'not_favorited_by':
            return 'not-favorited-by'
        case 'sort':
            return 'sort'
        case 'description_format':
            return 'description-format'
        case 'include_icon':
            return 'include-icon'
        case 'cursor':
            return 'cursor'
        case 'limit':
            return 'limit'
        case 'include_operations':
            return 'include-operations'
        case 'include_properties':
            return 'include-properties'
        case 'include_permissions':
            return 'include-permissions'
        case 'include_labels':
            return 'include-labels'
