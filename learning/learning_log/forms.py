from django import forms
from .models import Entry, Topic

class TopicForm(forms.ModelForm):# cria um formulário baseado no modelo Topic
    class Meta:
        model = Topic # indica que o formulário é baseado no modelo Topic
        fields = ['text'] # indica que o formulário vai ter apenas o campo text
        labels = {'text': 'escreva um novo tópico'} # indica o rótulo do campo text

class EntryForm(forms.ModelForm):# cria um formulário baseado no modelo Entry
    class Meta:
        model = Entry # indica que o formulário é baseado no modelo Entry
        fields = ['text'] # indica que o formulário vai ter apenas o campo text
        labels = {'text': 'diga o que você aprendeu'} # indica o rótulo do campo text
        widgets = {'text': forms.Textarea(attrs={'cols':80})} # indica que o campo text vai ser um textarea com 80 colunas