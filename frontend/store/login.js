export const state = () => ({
  showSignup: false,
});

export const mutations = {
  toggleShowSignup(state) {
    state.showSignup = !state.showSignup;
  },
};
