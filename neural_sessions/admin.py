from django.contrib import admin
import neural_sessions.models



class NeuralSessionInline(admin.StackedInline):
    """For a tab within GrandSession"""
    model = neural_sessions.models.NeuralSession
    
    # If fields unspecified, all are displayed
    fields = (
        'name',
        'data_directory',
        'sort_name',
        'recording_numbers',
        'adapter',
        'electrode',
        'manipulator_angle',
        'z_touch',
        'z_final',
        'z_withdraw',
        'exclude_channels',
        'notes',
        'channel_quality_notes',
    )
    
    suit_classes = 'suit-tab suit-tab-neural'

# Register your models here.
class NeuralSessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort_name', 'bsession',]

admin.site.register(neural_sessions.models.NeuralSession, NeuralSessionAdmin)
