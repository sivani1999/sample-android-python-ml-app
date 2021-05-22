package com.example.diabetesprediction;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;


import com.basgeekball.awesomevalidation.AwesomeValidation;
import com.basgeekball.awesomevalidation.ValidationStyle;
import com.google.common.collect.Range;

public class FormPage extends AppCompatActivity {
    EditText etName, etNop, etGl, etBp, etSt, etInsulin, etBmi, etDpf, etAge;

    //defining AwesomeValidation object
    AwesomeValidation awesomeValidation;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_form_page);

        awesomeValidation = new AwesomeValidation(ValidationStyle.BASIC);

        //Assign Edit Text variable
        etName = findViewById(R.id.et_name);
        etNop = findViewById(R.id.et_nop);
        etGl = findViewById(R.id.et_gl);
        etBp = findViewById(R.id.et_bp);
        etSt = findViewById(R.id.et_st);
        etInsulin = findViewById(R.id.et_insulin);
        etBmi = findViewById(R.id.et_bmi);
        etDpf = findViewById(R.id.et_dpf);
        etAge = findViewById(R.id.et_age);

        //adding validation to edittexts
        awesomeValidation.addValidation(this, R.id.et_name, "^[A-Za-z\\s]{1,}[\\.]{0,1}[A-Za-z\\s]{0,}$", R.string.nameerror);
        awesomeValidation.addValidation(this, R.id.et_nop, Range.closed(0, 17), R.string.noperror);
        awesomeValidation.addValidation(this, R.id.et_gl, Range.closed(1, 199), R.string.glerror);
        awesomeValidation.addValidation(this, R.id.et_bp, Range.closed(1, 122), R.string.bperror);
        awesomeValidation.addValidation(this, R.id.et_st, Range.closed(1, 99), R.string.sterror);
        awesomeValidation.addValidation(this, R.id.et_insulin, Range.closed(1, 846), R.string.insulinerror);
        awesomeValidation.addValidation(this, R.id.et_bmi, Range.closed(1, 68), R.string.bmierror);
        awesomeValidation.addValidation(this, R.id.et_dpf, Range.closed(1, 2), R.string.dpferror);
        awesomeValidation.addValidation(this, R.id.et_age, Range.closed(21, 81), R.string.ageerror);
    }
        public void MoveResult(View view) {
            String sname=etName.getText().toString();



        if (awesomeValidation.validate()) {
            Intent i=new Intent(FormPage.this,ResPage.class);
            i.putExtra("key",sname);
            startActivity(i);
        }
        }

    }

