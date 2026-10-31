---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-31
description: "Ezetimibe：預測新適應症為膽固醇酯轉運蛋白缺乏症 (cholesterol-ester transfer protein deficiency)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Ezetimibe
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

## Ezetimibe: 膽固醇酯轉運蛋白缺乏症 (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## 一句話總結

Ezetimibe 是一種降低膽固醇吸收的藥物，知識圖譜中記錄的相關用途為高脂血症、家族性高膽固醇血症與谷固醇血症。
TxGNN 模型預測它可能對**膽固醇酯轉運蛋白缺乏症 (Cholesterol-ester transfer protein deficiency)** 有效，但目前**沒有臨床試驗**，也沒有直接研究此疾病的文獻，證據僅停留在模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 膽固醇酯轉運蛋白缺乏症 (cholesterol-ester transfer protein deficiency) |
| TxGNN 預測分數 | 0.9909 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識，ezetimibe 抑制 NPC1L1 介導的腸道膽固醇吸收，進而降低 LDL-C。

膽固醇酯轉運蛋白（CETP）缺乏症是一種遺傳性狀況，特徵為 HDL-C 明顯升高與脂蛋白代謝改變。兩者的關聯僅在於同屬脂質代謝路徑，屬間接連結。

TxGNN 的高分是網路式預測，並無臨床資料支持。CETP 缺乏通常屬良性，甚至可能具保護性，並沒有明確需要降 LDL 治療的未滿足需求，因此再利用的理由薄弱，任何療效的機轉基礎都不明確。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻皆未直接研究 CETP 缺乏症，僅提供脂質代謝的背景資訊。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Review | European Heart Journal | 回顧降脂治療的標靶，說明 LDL-C、三酸甘油酯、apoB 與 Lp(a) 對殘餘心血管風險的重要性 |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | 動物研究 | International Journal of Molecular Sciences | 以異合子 Ldlr 缺陷倉鼠評估 PCSK9 抗體對高脂血症與動脈粥樣硬化的效果 |

## 香港上市資訊

以下為本報告所整理的部分許可證（清單可能不完整），資料中未載明劑型與核准適應症文字。單方許可證如下：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66209 | LIPEZ TABLETS 10MG | 未載明 | 未載明 |
| HK-65290 | ALZETIM TABLETS 10MG | 未載明 | 未載明 |
| HK-68102 | JECEZETIM TABLETS 10MG | 未載明 | 未載明 |
| HK-51223 | EZETROL TAB 10 MG | 未載明 | 未載明 |
| HK-63988 | PMS-EZETIMIBE TABLETS 10MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：胰臟炎、肝臟疾病、膽囊疾病、肌病變、肌肉疾病、骨骼肌疾病、家族性週期性麻痺、物質濫用/依賴、橫紋肌溶解症、結節性筋膜炎。
- **藥物交互作用**：共查得 100 筆，以下為中度等級者：
  - Chenodeoxycholic acid
  - Eluxadoline
  - Rosuvastatin
  - Simvastatin

  其餘多數交互作用等級不明。

仿單的警語與禁忌資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或直接研究 CETP 缺乏症的文獻，僅有模型預測（L5）。
- CETP 缺乏通常屬良性表型，缺乏明確的治療需求，機轉連結也只是間接的。

**若要推進需要：**
- 先釐清 CETP 缺乏症是否有需要降 LDL-C 的臨床族群與未滿足需求。
- 補充 ezetimibe 的作用機轉資料，並進行機轉層面的連結分析。
- 取得香港仿單的警語、禁忌與核准適應症文字，以進行安全性篩選。
- 若仍要探索，先從基礎或觀察性研究開始，再考慮臨床試驗。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

