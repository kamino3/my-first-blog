
# forms.py: このファイルでDjangoのフォームの定義が行われます。
# フォームはユーザーからの入力を受け取るためのインターフェースとして使用されます。
    from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text',)


class PostForm(ModelForm):
    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'tags']
