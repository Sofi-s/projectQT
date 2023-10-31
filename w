<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>819</width>
    <height>666</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 253, 240);</string>
  </property>
  <widget class="QWidget" name="formLayoutWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>341</width>
     <height>231</height>
    </rect>
   </property>
   <layout class="QFormLayout" name="formLayout">
    <item row="0" column="0">
     <widget class="QPushButton" name="yarkost">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 184);</string>
      </property>
      <property name="text">
       <string>Яркость</string>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QSlider" name="horizontalSlidery">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
    </item>
    <item row="1" column="0">
     <widget class="QPushButton" name="razmutie">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(219, 255, 252);</string>
      </property>
      <property name="text">
       <string>размытие</string>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QSlider" name="horizontalSlider_2">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
    </item>
    <item row="2" column="0">
     <widget class="QPushButton" name="prozrachnost">
      <property name="text">
       <string>прозрачность</string>
      </property>
     </widget>
    </item>
    <item row="2" column="1">
     <widget class="QSlider" name="horizontalSlider_3">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
    </item>
    <item row="3" column="0">
     <widget class="QPushButton" name="sepeia">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 153, 85);</string>
      </property>
      <property name="text">
       <string>сепия</string>
      </property>
     </widget>
    </item>
    <item row="3" column="1">
     <widget class="QSlider" name="horizontalSlider_4">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
    </item>
    <item row="4" column="0">
     <widget class="QPushButton" name="blue">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(41, 80, 255);</string>
      </property>
      <property name="text">
       <string>Цианотипия</string>
      </property>
     </widget>
    </item>
    <item row="4" column="1">
     <widget class="QSlider" name="horizontalSlider_5">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
    </item>
    <item row="5" column="0">
     <widget class="QPushButton" name="negative">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(12, 1, 0);
color: rgb(255, 255, 255);</string>
      </property>
      <property name="text">
       <string>негатив</string>
      </property>
     </widget>
    </item>
    <item row="5" column="1">
     <widget class="QSlider" name="horizontalSlider_6">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
    </item>
    <item row="6" column="0">
     <widget class="QPushButton" name="yellow">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 0);</string>
      </property>
      <property name="text">
       <string>желтый</string>
      </property>
     </widget>
    </item>
    <item row="6" column="1">
     <widget class="QSlider" name="horizontalSlider_7">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
    </item>
    <item row="7" column="0">
     <widget class="QPushButton" name="hb">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
      <property name="text">
       <string>чб</string>
      </property>
     </widget>
    </item>
    <item row="7" column="1">
     <widget class="QSlider" name="horizontalSlider_8">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>590</x>
     <y>620</y>
     <width>211</width>
     <height>31</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QPushButton" name="pushButton_10">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 184);</string>
      </property>
      <property name="text">
       <string>открыть изображение </string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_9">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 184);</string>
      </property>
      <property name="text">
       <string>сохранить</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>250</y>
     <width>121</width>
     <height>101</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLabel" name="povorot">
      <property name="font">
       <font>
        <family>Papyrus</family>
        <pointsize>12</pointsize>
       </font>
      </property>
      <property name="layoutDirection">
       <enum>Qt::RightToLeft</enum>
      </property>
      <property name="text">
       <string>поворот на</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pravod">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 184);</string>
      </property>
      <property name="text">
       <string>90 вправо</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="levod">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 184);</string>
      </property>
      <property name="text">
       <string>90 влево</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pravos">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 184);</string>
      </property>
      <property name="text">
       <string>180</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QLabel" name="izobr">
   <property name="geometry">
    <rect>
     <x>400</x>
     <y>20</y>
     <width>371</width>
     <height>301</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
