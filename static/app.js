new Vue({
  el: '#app',
  data: {
    currentTab: 1,
    articles: [
      {
        id: 1,
        title: 'Qiita風記事1',
        body: 'Qiita風記事1の内容がここに入ります。',
        created_at: '2023-07-31T12:34:56',
        user: {
          name: 'ユーザーA',
          avatar_url: 'https://via.placeholder.com/60'
        },
        url: 'https://example.com/article1'
      },
      {
        id: 2,
        title: 'Qiita風記事2',
        body: 'Qiita風記事2の内容がここに入ります。',
        created_at: '2023-07-30T10:20:30',
        user: {
          name: 'ユーザーB',
          avatar_url: 'https://via.placeholder.com/60'
        },
        url: 'https://example.com/article2'
      },
      // 他の記事も同様に設定...
    ]
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
    },
    changeTab(tabNumber) {
      this.currentTab = tabNumber;
    }
  }
});
