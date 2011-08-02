
def upgrade(context):
    context.runImportStepFromProfile('profile-plonetheme.globms:default',
                                     'typeinfo')
