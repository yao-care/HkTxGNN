---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 784
evidence_level: L5
indication_count: 10
monitor_inn: "ROMIPLOSTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
last_modified_at: 2026-10-23
description: "Romiplostim：預測新適應症為原發性血小板釋放障礙 (primary release disorder of platelets)（證據等級 L5）。原適應症：香港許可證未載明核准適應症"
---

# Romiplostim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Romiplostim：從免疫性血小板低下症到原發性血小板釋放障礙
{: .text-alpha }

## 一句話總結

Romiplostim 是一種血小板生成素受體（TPO 受體）促效劑，知識圖譜中記錄的相關用途包括再生不良性貧血與自體免疫性血小板低下症。
TxGNN 模型預測它可能對**原發性血小板釋放障礙 (primary release disorder of platelets)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**與此疾病並無直接關聯的機轉文獻，證據僅達 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症；知識圖譜中記錄的相關疾病為特發性再生不良性貧血、再生不良性貧血、自體免疫性血小板低下症 |
| 預測新適應症 | 原發性血小板釋放障礙 (primary release disorder of platelets) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。依據藥理資料，Romiplostim 作用於血小板生成素受體（基因 MPL, c-Mpl），可刺激巨核細胞成熟並增加血小板生成，主要用於以血小板數量不足為特徵的免疫性血小板低下症。

然而，原發性血小板釋放障礙屬於**血小板功能缺陷**（顆粒分泌或活化受損），問題不在血小板數量。提高血小板數量，預期無法矯正其功能缺陷。

TxGNN 模型（深度學習）對 primary release disorder of platelets（血小板釋放障礙）給出 1.0000 的極高分數，這可能反映模型從相關疾病之間學到的相似性，而非生物學證據。唯一檢索到的文獻探討的是 ITP 自體抗體抑制前血小板形成，並非此疾病特有，因此不宜視為支持證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | 基礎機轉研究 | Haematologica | ITP 患者的抗血小板自體抗體會抑制巨核細胞的前血小板形成並影響血小板生成（研究對象為 ITP，非本預測疾病） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63777 | ROMIPLATE POWDER FOR SOLUTION FOR INJECTION 250MCG | 未載明 | 未載明 |

## 安全性考量

- **藥物交互作用**：資料庫中記錄與 Carfilzomib 有 Major 等級的交互作用。另有藥理資料顯示 Romiplostim 的作用標的為血小板生成素受體（此為標的資訊，並非交互作用等級）。

其他警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測純屬計算結果，無臨床試驗，也無直接研究此疾病的文獻，證據等級為 L5。
- 此疾病為血小板功能缺陷而非數量不足，TPO 受體促效劑缺乏明確的機轉依據。

**若要推進需要：**
- 取得完整的作用機轉資料與香港仿單的警語、禁忌症與核准適應症
- 釐清此疾病是否存在血小板生成不足的亞群，並進行機轉與病例層級的研究
- 若要探索血小板數量不足的相關疾病（如胎兒與新生兒同種免疫性血小板低下症，目前為 L4 的研究問題），應另行以專屬證據評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

