from core.data_matrix import DataMatrix

def get_default_data():
    return DataMatrix({
        'Is it a change?': [
            'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 
            'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 
            'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 
            'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'
        ],
        'Does it apply to Special Characteristics towards the customer?': [
            'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
            'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
            'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
            'N', 'N', 'N', 'N', 'N', 'N', 'N/A', 'N/A', 'N/A'
        ],
        'Does it apply to the technical interface to the customer?': [
            'N/A', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
            'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
            'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
            'N', 'N', 'N', 'N', 'N', 'N', 'N/A', 'N/A', 'N/A'
        ],
        'Change type?': [
            'N/A', 'N/A', 'Design', 'Design', 'Design', 'Design', 'Design', 'Design', 'Design', 'Design',
            'Design', 'Design', 'Process', 'Process', 'Process', 'Process', 'Process', 'Process', 'Process', 'Process',
            'Process', 'Process', 'Process', 'Process', 'Process', 'Process', 'Process', 'Process', 'Process', 'Logistics',
            'Logistics', 'Logistics', 'Logistics', 'Document', 'Document', 'Document', 'N/A', 'N/A', 'N/A'
        ],
        'Does it apply to contract documents?': [
            'N/A', 'N/A', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N',
            'N', 'N', 'Y', 'Y', 'N', 'N', 'N', 'N', 'N', 'N',
            'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y',
            'N', 'N', 'N', 'Y', 'N', 'N', 'N/A', 'N/A', 'N/A'
        ],
        'Does it apply to fit, form, function, performance, reliability?': [
            'N/A', 'N/A', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N',
            'N', 'N', 'N/A', 'N/A', 'Y', 'Y', 'N', 'N', 'N', 'N',
            'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N/A',
            'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
        ],
        'Section': [
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, 'Manufacturing/Assembly', 'Manufacturing/Assembly', 'Manufacturing/Assembly', 'Manufacturing/Assembly',
            'Manufacturing/Assembly', 'Manufacturing/Assembly', 'Testing', 'Testing', 'Testing', 'Testing',
            'Production Relocation', 'Production Relocation', 'Production Relocation', None, None, None, None, None, None, None, None, None, None
        ],
        'Result': [
            'Ch in the Special Characteristics of the product, component (electric/mechanical), production process, etc. specified with the customer, ... ',
            'e.g. attachment to vehicle, electron. connections, electron. components, ...',
            'e.g. Ch in design, tools, ...',
            'e.g. Ch in product software through (changed) functional software requirements',
            'e.g. Ch in product software through (changed) non-functional software requirements',
            'e.g. Ch in sealing material, Ch in an EMC capacitor, ...',
            'e.g. Ch of dimension not contained in the customer drawing',
            'Ch of substance / material ',
            'Ch in requirements of internal specs or tolerance change, outside of customer spec',
            'Ch in requirements of internal specs or tolerance change, still within customer spec',
            'Ch of name / designation of parts / materials with same composition',
            'Ch in roughing levels (e.g. pre-roughing dimension of a shaft, reception of wafers, ...)',
            'e.g. Ch in the process chain (including supplier, duplication of production lines, ...)',
            'e.g. Ch of test, test flow or other reasons, ...',
            'e.g. Ch in curing parameters, injection temperature, ...',
            'e.g. Ch in the process chain (including supplier, duplication of production lines, ...)',
            'Ch in number of cavities in tool, follow-on/enhancement tools',
            'Duplication of production and test equipment within an existing line',
            'Procurement and use of a new machine type',
            'Ch to existing tool, new device, new poka-yoke',
            'Ch to process including roughing levels (as in no.12)',
            'Ch of setting parameters, operating equipment, injection temperature, ...',
            'Ch in test method, risk higher',
            'Ch in test method, risk unchanged / lower, same process sequence',
            'Expansion of testing without method change (e.g. increase in samples)',
            'Reduction / elimination of test not relevant to customer (e.g. sampling)',
            'Tools from line to line, equivalent lines  ',
            'Relocation of facilities with mobile design within a production plant without changing process chain',
            'Location Ch: relocation of facilities, parallel production (not for roughing levels as in no.12)',
            'Ch of supplier, new second supplier, supplier changes sub-supplier',
            'New forwarder or ESP, SLC',
            'Packaging towards the customer, shipping, invoicing ',
            'Internal packaging (e.g. plant-plant, in-house, ...) and sub-suppliers ',
            'Document adaptation to condition of approved product',
            'Document adaptation to condition of approved product or correction of formal errors ',
            'Ch in non-product-related documents (e.g. work instructions, ...)',
            'Reuse of lines, facilities, machines, tools, cavities, and molds after a standstill of 12 months or more**',
            'Maintenance / servicing of existing tools, tools subject to rapid wear (e.g. lathe tools, honing mandrels)',
            'Replacement of identical or functionally equivalent machine, replacement of identical test equipment'
        ],
        'Symbol': [
            'A', 'A', 'A', 'A', 'I', 'A', 'A', 'A', 'A', '-',
            '-', '-', 'A', 'A', 'A', 'A', 'I', 'I', 'I', '-',
            '-', '-', 'U', 'I', '-', '-', '-', '-', 'A', 'A',
            'I', 'A', '-', 'A', '-', '-', 'A', '-', '-'
        ],
        'Line': [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39
        ]
    })