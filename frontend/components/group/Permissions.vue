<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>Permissões</strong>
    </div>
    <div class="tile is-child is-9 permissions">
      <div class="select-perms">
        <b-field>
          <b-select
            v-model="selectPermissionsFrom"
            multiple
            size="10"
            native-size="10"
          >
            <option
              v-for="permission in permissions_from"
              :key="permission.id"
              :value="permission.id"
              >{{ permission.name }}</option
            >
          </b-select>
        </b-field>
        <b-button
          type="is-info"
          icon-right="arrow-right-bold-outline"
          @click="selectAllPerm"
          >Escolher todos</b-button
        >
      </div>
      <div class="select-buttons">
        <b-button
          type="is-info"
          icon-right="arrow-right-bold-outline"
          @click="selectPerm"
        ></b-button>
        <b-button
          type="is-info"
          icon-right="arrow-left-bold-outline"
          @click="removePerm"
        ></b-button>
      </div>
      <div class="select-perms">
        <b-field>
          <b-select v-model="selectPermissionsTo" multiple native-size="10">
            <option
              v-for="permission in choosed_permissions"
              :key="permission.id"
              :value="permission.id"
              >{{ permission.name }}</option
            >
          </b-select>
        </b-field>
        <b-button
          type="is-info"
          icon-right="arrow-left-bold-outline"
          @click="removeAllPerm"
          >Remover todos</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    choosedIds: Array,
    edit: {
      type: Boolean,
      default() {
        return false
      }
    }
  },
  async fetch() {
    this.permissions = await this.$axios.$get('/api/v1/permissions/')
  },
  data() {
    return {
      selectPermissionsFrom: [],
      selectPermissionsTo: [],
      permissions: []
    }
  },
  computed: {
    permissions_from() {
      let choosed = this.choosedIds

      var perms = this.permissions.filter(function (permission) {
        return choosed.includes(permission.id) == false
      })
      return perms
    },
    choosed_permissions() {
      let choosed = this.choosedIds
      var perms = this.permissions.filter(function (permission) {
        return choosed.includes(permission.id)
      })
      return perms
    }
  },
  methods: {
    selectPerm() {
      this.choosedIds = [...this.choosedIds, ...this.selectPermissionsFrom]
      this.selectPermissionsFrom = []
      this.$emit('update-choosed', this.choosedIds)
    },
    selectAllPerm() {
      this.choosedIds = [
        ...this.choosedIds,
        ...this.permissions_from.map(({ id }) => id)
      ]
      this.selectPermissionsFrom = []
      this.$emit('update-choosed', this.choosedIds)
    },
    removePerm() {
      this.choosedIds = this.choosedIds.filter(
        id => !this.selectPermissionsTo.includes(id)
      )
      this.selectPermissionsTo = []
      this.$emit('update-choosed', this.choosedIds)
    },
    removeAllPerm() {
      this.choosedIds = []
      this.selectPermissionsTo = []
      this.$emit('update-choosed', this.choosedIds)
    }
  }
}
</script>

<style>
.permissions {
  display: flex;
  height: 400px;
}
.select-perms {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 40%;
}

.select-buttons {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin-top: 100px;
}

.select-buttons button {
  margin-bottom: 10px;
}
</style>
