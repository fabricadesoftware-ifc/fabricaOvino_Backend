<template>
  <form @submit.prevent="submit">
    <input id="category-id" v-model="value.id" type="hidden" />
    <b-field
      :label="$t('pages.admin.forms.name.label')"
      message="Nome da categoria"
      horizontal
    >
      <b-input
        v-model="value.name"
        :placeholder="$t('pages.admin.forms.name.placeholder')"
        type="text"
        icon="tag"
        required
      />
    </b-field>
    <b-field horizontal>
      <b-field grouped>
        <div class="control">
          <b-button native-type="submit" type="is-primary">{{
            $t('buttons.save')
          }}</b-button>
        </div>
        <div class="control">
          <b-button type="is-primary is-outlined" @click="reset">{{
            $t('buttons.reset')
          }}</b-button>
        </div>
      </b-field>
    </b-field>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props: {
    value: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  methods: {
    ...mapActions('categories', ['getCategories']),
    async submit() {
      try {
        const method = this.value.id ? 'put' : 'post'
        const id = this.value.id ? `/${this.value.id}` : ''
        const url = `/api/v1/categories${id}/`
        await this.$axios[method](url, this.value)
        this.$toasted.global.defaultSuccess()
        this.getCategories()
        this.reset()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    },
    reset() {
      this.$router.push({
        name: `category___${this.$i18n.locale}`
      })
    }
  }
}
</script>

<style></style>
