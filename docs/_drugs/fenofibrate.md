---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 1
monitor_inn: "FENOFIBRATE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-28
description: "Fenofibrate：預測新適應症為膽固醇酯轉運蛋白缺乏症（證據等級 L5）。原適應症：知識圖譜記錄的關聯：高三酸甘油脂血症、高脂血症、家族性高脂血症、低 α 脂蛋白血症"
---

# Fenofibrate
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

## Fenofibrate：從高三酸甘油脂血症到膽固醇酯轉運蛋白缺乏症
{: .text-alpha }

## 一句話總結

Fenofibrate 是一種 PPAR-alpha 促效劑，知識圖譜中記錄其與高三酸甘油脂血症、高脂血症等血脂異常相關。
TxGNN 模型預測它可能對**膽固醇酯轉運蛋白缺乏症 (Cholesterol-ester Transfer Protein Deficiency)** 有效，
但目前**沒有臨床試驗**，僅有 **3 篇**前臨床或機轉性文獻，且皆未直接研究此疾病，證據偏弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：高三酸甘油脂血症、高脂血症、家族性高脂血症、低 α 脂蛋白血症（許可證資料未載明核准適應症文字） |
| 預測新適應症 | 膽固醇酯轉運蛋白缺乏症 |
| TxGNN 預測分數 | 0.9961 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 19 張／共 19 張） |
| 許可證數 | 19 張（有效 19 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊與所收集的文獻，Fenofibrate 屬於 PPAR-alpha 促效劑，可提升 HDL-C 並降低三酸甘油脂，作用包括上調 ApoA-I／ApoA-II 與脂蛋白脂解酶，以及誘導磷脂轉運蛋白 (PLTP) 表現（PMID 11342537）。

膽固醇酯轉運蛋白缺乏症的特徵是 HDL-C 顯著升高、膽固醇酯轉運受損。Fenofibrate 與此疾病的連結屬於間接的藥理學關聯：兩者涉及重疊的 HDL 代謝路徑（PLTP、HDL 重塑），且有研究將 fenofibrate 與 CETP 抑制劑併用於小鼠（PMID 20332533）。然而，沒有證據顯示 fenofibrate 能治療 CETP 缺乏狀態。

此外，CETP 缺乏本身已呈現高 HDL-C，使用升 HDL 的藥物臨床理由並不明確。0.996 的高分較可能反映脂質代謝基因在網絡上的鄰近性，而非已驗證的療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | 前臨床／機轉研究 | J Cardiovasc Pharmacol Ther | 在表現人類 ApoB-100 與 CETP 的基因轉殖小鼠中，CETP 抑制（torcetrapib）合併 PPARα 促效（fenofibrate）可提升 HDL-C 並降低 LDL-C |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | 前臨床／機轉研究 | J Biol Chem | 小鼠經 fenofibrate 處理後，PLTP 基因被誘導，造成 HDL 增大 |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | 機轉／觀察性研究 | Front Physiol | 血漿 HDL 與糞便膽固醇排出及膽固醇流出能力缺乏相關，顯示 HDL 功能的重要性 |

以上文獻皆未直接研究膽固醇酯轉運蛋白缺乏症的患者或治療效果。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59427 | FENOGET CAP 200MG | — | 許可證資料未載明 |
| HK-50649 | LIPANTHYL SUPRA TAB 160MG | — | 許可證資料未載明 |
| HK-53289 | LEXEMIN CAP 100MG | — | 許可證資料未載明 |
| HK-59426 | FENOGET CAP 67MG | — | 許可證資料未載明 |
| HK-67885 | LIPANTHYL MICRO CAPSULES 267MG | — | 許可證資料未載明 |

此處僅列出 5 張主要許可證，其餘共 19 張。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：肝衰竭、肝病、胰臟炎、膽囊疾病、膽結石、血小板減少、肌病變與橫紋肌溶解、腎功能受損、貧血，以及白血球減少、嗜中性球低下等血液疾病。
- **藥物交互作用**：資料庫共查得 100 筆，以下為列出的中度交互作用：
  - 降血糖藥：acetohexamide、chlorpropamide、glimepiride、glipizide、glyburide
  - 各類胰島素（人類胰島素、aspart、degludec、detemir、glargine、glulisine、lispro 等）
  - 其他：chenodeoxycholic acid、esomeprazole

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何直接研究此疾病的臨床試驗或文獻，證據等級僅為 L5，預測主要來自模型分數。
- 此疾病本身已有高 HDL-C，使用升 HDL 的藥物臨床理由不明確。

**若要推進需要：**
- 釐清 CETP 缺乏症中使用 fenofibrate 的臨床目標（例如是否為合併高三酸甘油脂血症的情況）
- 取得詳細的作用機轉資料與香港仿單的警語、禁忌資料
- 針對 CETP 缺乏症患者或相關模型進行直接研究，再重新評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

