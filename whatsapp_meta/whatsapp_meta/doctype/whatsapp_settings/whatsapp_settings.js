// Copyright (c) 2023, Ragul KM and contributors
// For license information, please see license.txt

frappe.ui.form.on('Whatsapp Settings', {
	refresh: function (frm) {
		if (frm.doc.access_token && frm.doc.phone_number_id) {
			frm.add_custom_button('Verify Token', () => {
				set_primary_action(frm);
			}).addClass("btn-primary");
		}
	}
});

function set_primary_action(frm) {
	frappe.prompt({
		label: 'WhatsApp Number',
		fieldname: 'phone_number',
		fieldtype: 'Data',
		description: 'WhatsApp number with country code(eg: 91)',
		reqd: 1
	}, (values) => {
		send_verify_message(frm, values.phone_number)
	})
}

function send_verify_message(frm, phone_number) {
	frappe.call({
		method: 'whatsapp_meta.whatsapp_meta.doctype.whatsapp_cloud_settings.whatsapp_cloud_settings.send_test_message',
		args: {
			"phone_number": phone_number
		},
		callback: function (r) {
			if (r && r.message) {
				frappe.msgprint({
					title: __('Success'),
					message: __("WhatsApp Account successfully configured. <br> Message ID : {0}", [r.message])
				});
			}
		},
		freeze: true,
		freeze_message: ('Sending WhatsApp test Message.!!')
	});
}
