export const state = () => ({
  feeds: []
})

export const mutations = {
  leadFeeds(state, feeds) {
    state.feeds = feeds
  }
}

export const actions = {
  async getFeeds({ commit }) {
<<<<<<< HEAD
    const feeds = await this.$axios.$get('/api/v1/feeds')
=======
    const feeds = await this.$axios.$get('api/v1/feeds')
>>>>>>> origin/Dev-Maria
    commit('loadFeeds', feeds)
  }
}
