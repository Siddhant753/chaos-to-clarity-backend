from django.db import models

class RawInput(models.Model):
    raw_text = models.TextField() # Unstructured Input
    source = models.CharField(max_length= 100, blank= True, null= True) # Human, Machine, Logs, Vendors, etc.
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.raw_text[:50]
    
class ProcessedEntry(models.Model):
    CATEGORY_CHOICES = [
        ('Incident','Incident'),
        ('Vendor Issue','Vendor Issue'),
        ('QA Issue','QA Issue'),
        ('Electrical','Electrical'),
        ('Mechanical','Mechanical'),
        ('Environmental','Environmental'),
        ('Uncategorized','Uncategorized'),
    ]

    raw_input = models.ForeignKey(RawInput, on_delete= models.CASCADE, related_name= 'processed')
    category = models.CharField(max_length= 50, choices= CATEGORY_CHOICES)
    tags = models.JSONField(default= list)
    severity = models.CharField(max_length= 20)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add= True)