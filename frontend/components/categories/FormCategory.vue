<template>
  <div class="form">
    <input type="hidden" id="category-id" v-model="value.id" />
    <b-field
      :label="$t('pages.admin.forms.name.label')"
      class="category-form-fields"
    >
      <b-input
        :placeholder="$t('pages.admin.forms.name.placeholder')"
        type="text"
        icon="tag"
        v-model="value.name"
        required
      />
    </b-field>
    <div class="category-form-buttons">
      <b-button type="is-info" icon-left="check" @click="save">
        {{ $t('buttons.save') }}
      </b-button>
      <b-button type="is-dark" icon-left="redo" @click="reset">
        {{ $t('buttons.reset') }}
      </b-button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props: {
    value: Object
  },
  methods: {
    ...mapActions('categories', ['getCategories']),
    async save() {
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
