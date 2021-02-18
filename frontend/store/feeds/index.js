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
    const feeds = await this.$axios.$get('/api/v1/feeds')
    commit('loadFeeds', feeds)
  }
}
