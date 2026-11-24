---
layout: default
title: Potassium Acetate
parent: 僅模型預測 (L5)
nav_order: 716
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Potassium Acetate：預測新適應症為腎小管酸中毒 (Renal Tubular Acidosis)（證據等級 L5）。原適應症：鉀缺乏症 (Potassium Deficiency Disease)"
monitor_inn: "POTASSIUM ACETATE"
predicted_indications: ["renal tubular acidosis"]
---

# Potassium Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Potassium Acetate：從鉀缺乏症到腎小管酸中毒
{: .text-alpha }

## 一句話總結

Potassium Acetate（醋酸鉀）是一種鉀鹽，原本用於治療鉀缺乏症。
TxGNN 模型預測它可能對**腎小管酸中毒 (Renal Tubular Acidosis)** 有效，
但目前**沒有臨床試驗和文獻**支持，僅有模型預測，屬於待驗證的研究假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鉀缺乏症 (Potassium Deficiency Disease) |
| 預測新適應症 | 腎小管酸中毒 (Renal Tubular Acidosis) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 10 張／共 10 張） |
| 許可證數 | 10 張（有效 10 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，醋酸鉀是補充鉀離子的電解質鹽類，其在鉀缺乏症中的用途已被確立。醋酸根在體內可代謝為碳酸氫根（bicarbonate），因此理論上同時具備補鉀與鹼化的作用。

腎小管酸中毒（特別是遠端／第 1 型）常伴隨低血鉀與代謝性酸中毒。目前標準做法是使用鹼性藥物（如檸檬酸鉀或碳酸氫鈉）來矯正，因此「補鉀加鹼化」的概念在機轉上有合理之處。

但需要強調：這個關聯是**推論而非已證實**。沒有任何資料顯示醋酸鉀優於現有的鉀鹽或鹼化劑。在近端型或高血鉀型（第 4 型）腎小管酸中毒，額外的鉀負荷反而可能有害，使用上需特別謹慎。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-65534 | PLASMA-LYTE 56 ELECTROLYTE SOLUTION IN 5% W/V GLUCOSE IV INFUSION | 複方 | BAXTER HEALTHCARE LIMITED | 有效 |
| HK-61211 | AMINOPLASMAL B. BRAUN 10% E SOLUTION FOR INFUSION | 複方 | B. BRAUN MEDICAL (HK) LTD | 有效 |
| HK-65813 | NUMETA G13% E PRETERM EMULSION FOR INFUSION 300ML | 複方 | BAXTER HEALTHCARE LIMITED | 有效 |
| HK-50080 | NUTRIFLEX LIPID PERI EMULSION FOR INF. | 複方 | B. BRAUN MEDICAL (HK) LTD | 有效 |
| HK-67635 | OMEGAFLEX SPECIAL EMULSION FOR INFUSION | 複方 | B. BRAUN MEDICAL (HK) LTD | 有效 |

上表列出其中 5 張（共 10 張）。

<!-- licenses:end -->

以上為其中部分許可證，皆為複方；張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。

<!-- review:begin hk-lic-20261124b-potassium_acetate-1 -->

> **查核更正（2026-11-24）**：原文為「以上為 10 張許可證中的 5 張，均為單一成分、現行有效的許可證，無已註銷者。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證皆為複方；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-potassium_acetate-1 -->

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 40 筆交互作用，其中較重要者如下：
  - **重大 (Major)**：Amiloride（保鉀利尿劑）、Benazepril（ACE 抑制劑）、Olmesartan、Valsartan、Azilsartan medoxomil（ARB 類）。這些藥物與鉀補充併用，可能導致高血鉀。
  - **中度 (Moderate)**：Aliskiren。
  - **輕微 (Minor)**：多種胰島素製劑（如 Insulin aspart、glargine、lispro、human 等）。

其他警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測分數（0.9990），沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- 作用機轉資料缺漏，且仿單的警語與禁忌症尚未取得，無法進行安全性評估。現有鹼化劑與鉀鹽已是標準治療，醋酸鉀的額外價值不明。

**若要推進需要：**
- 補齊醋酸鉀的作用機轉資料。
- 取得香港衛生署的仿單，確認警語與禁忌症，並補充各許可證的劑型與核准適應症。
- 進行文獻與臨床試驗的系統性檢索，確認是否有醋酸鉀用於腎小管酸中毒的研究。
- 釐清適用的腎小管酸中毒亞型（如第 1 型），並排除高血鉀風險族群（如第 4 型）。
- 評估與檸檬酸鉀、碳酸氫鈉相比的優勢，以及給藥途徑的相容性。
- 針對與保鉀利尿劑、ACE 抑制劑、ARB 併用的情形，擬定血鉀監測計畫。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「以上為 10 張許可證中的 5 張，均為單一成分、現行有效的許可證，無已註銷者。」→「以上為其中部分許可證，皆為複方；張數與有效張數見」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

