---
layout: default
title: Sodium Acetate
parent: 僅模型預測 (L5)
nav_order: 818
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sodium Acetate：預測新適應症為先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)（證據等級 L5）。原適應症：香港許可證未載明核准適應症"
monitor_inn: "SODIUM ACETATE"
predicted_indications: ["congenital prothrombin deficiency", "epiglottitis", "urinary tract infection (disease)", "sclerosing cholangitis", "gonococcal urethritis"]
---

# Sodium Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sodium Acetate：從電解質補充到先天性凝血酶原缺乏症

## 一句話總結

Sodium Acetate（醋酸鈉）是一種電解質與鈉／碳酸氫鹽前驅物來源，常見於輸液與腹膜透析液等複方製劑中。
TxGNN 模型預測它可能對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症 |
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，醋酸鈉是電解質輸液與透析液的成分，用來補充鈉，並在體內代謝後產生碳酸氫鹽，協助矯正酸鹼與電解質失衡。

先天性凝血酶原缺乏症是凝血因子 II 不足所致的凝血疾病，治療須靠因子補充（如凝血酶原複合物濃縮劑或血漿）。醋酸鈉的電解質功能與此疾病的病理沒有明顯關聯，我們**找不到合理的機轉連結**。

0.9998 的高分很可能是知識圖譜運算的假象，缺乏生物學支持。其他排名前列的預測（會厭炎、泌尿道感染、硬化性膽管炎、淋球菌性尿道炎）同樣沒有試驗或文獻佐證，機轉上也牽強。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

資料中共有 20 張有效許可證，皆為單一成分製劑，以下列出 5 張主要許可證。劑型與核准適應症欄位在登記資料中均為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-41852 | LACTATED RINGER'S INJ | LUEN CHEONG HONG LTD |
| HK-54146 | LACTATED RINGER'S INJ | OTSUKA PHARMACEUTICAL (H.K.) LIMITED |
| HK-28245 | COMPOUND SODIUM LACTATE INJ (HARTMANN'S) | B. BRAUN MEDICAL (HK) LTD |
| HK-62680 | DIANEAL PD-2 PERITONEAL DIALYSIS SOLUTION WITH 1.5% DEXTROSE (ULTRA BAG) | VANTIVE HEALTHCARE LIMITED |
| HK-64576 | PLASMA-LYTE 148 APPROX. PH 7.4 IV INFUSION | BAXTER HEALTHCARE LIMITED |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物－疾病關聯，非仿單內容）：腎臟病（含慢性腎臟病、慢性腎衰竭、末期腎病）、無尿症、心臟病與心血管疾病、房室傳導阻滯、心室顫動、洋地黃中毒、高血鈣與腎鈣沉著症、腎結石、高鉀性週期性麻痺、醛固酮低下症、苯丙酮尿症等。
- **藥物交互作用**：共查得 30 筆，以下為已列出的主要項目。
  - 中度：Doxycycline、Tetracycline、Minocycline、Acetylsalicylic acid、Choline salicylate、Ephedrine、Pseudoephedrine、Amphetamine、Dextroamphetamine、Benzphetamine、Methenamine
  - 輕度：Chlorpropamide、Tolazamide、Tolbutamide、Glipizide、Glyburide、Acetohexamide、Memantine、Methotrexate

仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 醋酸鈉是電解質來源，與凝血因子 II 缺乏在機轉上沒有合理連結，高分應視為圖譜假象。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料，並補齊作用機轉資料
- 進行系統性文獻檢索，確認是否存在任何支持性的前臨床或臨床證據
- 若無新證據，建議不再投入資源，並可改為檢視其他排名預測（如泌尿道感染，僅有尿液鹼化的推測性連結）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

