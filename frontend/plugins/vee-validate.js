import { extend } from 'vee-validate'
import { required, confirmed } from 'vee-validate/dist/rules'
extend('required', {
  ...required,
  message: 'This field is required'
})

extend('confirmed', {
  ...confirmed,
  message: 'This field confirmation does not match'
})
