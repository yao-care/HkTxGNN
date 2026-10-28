---
layout: default
title: Lovastatin
parent: 僅模型預測 (L5)
nav_order: 543
evidence_level: L5
indication_count: 1
monitor_inn: "LOVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Lovastatin：預測新適應症為膽固醇酯轉運蛋白缺乏症 (Cholesterol-ester transfer protein deficiency)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯為高三酸甘油酯血症、高脂血症、家族性高脂血症、動脈硬化、粥樣硬化等"
---

# Lovastatin
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

## Lovastatin：從高三酸甘油酯血症到膽固醇酯轉運蛋白缺乏症
{: .text-alpha }

## 一句話總結

Lovastatin 是一種史他汀類（statin）降血脂藥物，知識圖譜中記錄的使用方向為高脂血症、動脈粥樣硬化等脂質相關疾病。
TxGNN 模型預測它可能對**膽固醇酯轉運蛋白缺乏症 (Cholesterol-ester transfer protein deficiency)** 有效，
但目前**沒有臨床試驗**，且僅有 **1 篇**間接相關的前臨床文獻，證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯為高三酸甘油酯血症、高脂血症、家族性高脂血症、動脈硬化、粥樣硬化等（香港許可證未提供核准適應症文字） |
| 預測新適應症 | 膽固醇酯轉運蛋白缺乏症 (Cholesterol-ester transfer protein deficiency) |
| TxGNN 預測分數 | 0.9942 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識而言，Lovastatin 屬於 HMG-CoA 還原酶抑制劑，可降低肝臟膽固醇合成與 LDL 膽固醇。

膽固醇酯轉運蛋白（CETP）缺乏症是一種脂質代謝異常，特徵為 HDL 膽固醇偏高，以及脂蛋白間膽固醇酯轉運受損。兩者同屬脂質代謝路徑，這很可能是模型給出極高分數（0.9942）的原因。

然而，目前沒有直接的機轉或臨床證據顯示 Lovastatin 對此疾病有益。CETP 缺乏症多屬良性，甚至可能具心血管保護性，因此是否有治療需求並不明確。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19965609](https://pubmed.ncbi.nlm.nih.gov/19965609/) | 2010 | 前臨床（動物模型） | Journal of lipid research | 剔除 StARD4 基因的小鼠體重略減、脂質代謝僅有輕微變化；此研究並未直接探討 Lovastatin 或 CETP 缺乏症 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61102 | OVASTAR TAB 20MG | 未提供 | 未提供 |
| HK-39329 | MEDOSTATIN TAB 20MG | 未提供 | 未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：肝病、膽囊疾病、血小板低下、高血糖、消化性潰瘍、肌病變、橫紋肌溶解、糖尿病、糖尿病酮酸中毒、低血壓、痛風、物質濫用或依賴、凝血疾病、急性冠心症、冠狀動脈疾病、心肌梗塞等。
- **藥物交互作用**（共查得 100 筆，以下列出主要者）：
  - 重大：Clarithromycin
  - 中度：Aprepitant、Omeprazole、Esomeprazole、Lansoprazole、Pantoprazole、Metronidazole、Tinidazole、Cimetidine、Clotrimazole、Miconazole、Rosuvastatin、Simvastatin、Troglitazone 等
  - 輕微：Exenatide

詳細警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但無臨床試驗，唯一文獻為不直接相關的前臨床研究，證據等級為 L5。
- CETP 缺乏症多屬良性，臨床治療需求不明；加上作用機轉與仿單安全資料缺漏，目前不宜推進。

**若要推進需要：**
- 補充 Lovastatin 的作用機轉資料，並釐清其與 CETP 缺乏症的具體機轉關聯
- 確認 CETP 缺乏症是否有明確的臨床治療需求與可評估的療效指標
- 取得香港仿單的警語、禁忌與核准適應症資訊
- 搜尋是否有直接探討 statin 於 CETP 缺乏症患者的研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

