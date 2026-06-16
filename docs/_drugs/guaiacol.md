---
layout: default
title: Guaiacol
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 2
---

# Guaiacol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Guaiacol：從祛痰防腐成分到急性咽喉炎

## 一句話總結

Guaiacol（癒創木酚，2-甲氧基苯酚）為苯酚衍生物，歷史上曾作為祛痰與防腐輔助成分使用於咽喉製劑，目前在香港尚無以單一成分藥品形式上市的記錄。
TxGNN 模型預測它可能對**急性咽喉炎 (Acute Laryngopharyngitis)** 有效，
然而目前**完全缺乏**針對此適應症的臨床試驗或文獻支持，屬於純計算預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 歷史上作為祛痰／防腐輔助成分（無正式核准適應症記錄） |
| 預測新適應症 | 急性咽喉炎 (Acute Laryngopharyngitis) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Guaiacol（癒創木酚，CAS 90-05-1）是一種苯酚衍生物，化學名稱為 2-甲氧基苯酚（2-methoxyphenol），天然存在於癒創木（guaiac wood）樹脂及丁香等植物精油中。由於缺乏詳細的正式 MOA 資料，依據已知歷史紀錄，Guaiacol 曾廣泛作為咽喉製劑的祛痰與輕度防腐成分，其作用被認為與刺激支氣管及咽喉黏膜腺體分泌、降低黏液黏度，並具輕度抗菌活性有關。

TxGNN 模型給出的高預測分數（0.9957）主要反映知識圖譜中「祛痰藥 → 上呼吸道感染」的拓撲關聯。急性咽喉炎（acute laryngopharyngitis）的病理特徵涉及咽喉黏膜炎症與分泌物積聚，理論上與 Guaiacol 的祛痰機轉具有關聯性。

尤其值得關注的是，Guaiacol 的衍生物 **Guaifenesin**（甘油癒創木酚醚，glyceryl guaiacolate）已是全球廣泛使用的非處方祛痰藥；Guaifenesin 即由 Guaiacol 與甘油縮合而成，兩者共享促纖毛黏液清除的核心機轉。這間接為 Guaiacol 本體在呼吸道黏膜疾病方面的生物學合理性提供了佐證。然而，目前完全缺乏針對 Guaiacol 本體用於急性咽喉炎的臨床試驗或文獻，此預測屬純計算結果，尚待實驗驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

> **補充：第二預測適應症（鼻腔疾病）間接相關試驗**
>
> TxGNN 同時預測 Guaiacol 可能對**鼻腔疾病（Nasal Cavity Disease，預測分數 99.51%）**有效，並找到 1 個間接相關的臨床試驗（試驗藥物為 Guaiacol 衍生物 Guaifenesin，而非 Guaiacol 本體）：
>
> | 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
> |---------|------|------|------|---------|
> | [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | 完成 | 30 | 口服 Guaifenesin 用於 7-18 歲兒童慢性鼻炎的 14 天隨機雙盲對照試驗，以 SN-5 問卷評估鼻腔症狀改善及鼻分泌物生物物理特性。試驗藥物為 Guaifenesin（Guaiacol 結構衍生物），可作為祛痰機轉可行性之間接佐證，但不得直接外推至 Guaiacol 本體的有效性或安全性。 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Guaiacol 目前在香港**未以單一成分藥品形式上市**，無任何藥品許可證記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前完全缺乏 Guaiacol 本體用於急性咽喉炎的臨床試驗或文獻支持，證據等級僅為 L5（純模型預測），尚未達到啟動正式再利用評估的門檻。
- Guaiacol 在香港未以單一藥品形式上市，缺乏系統性人體安全性資料，且 MOA 資料存在資料缺口，無法進入安全性初評（S1 決策階段）。

**若要推進需要：**
- 查詢 DrugBank API（DB11359）取得完整作用機轉（MOA）、毒理學及藥動學資料
- 系統性文獻搜尋：Guaiacol 在呼吸道疾病的體外及動物實驗研究
- 評估 Guaifenesin 相關臨床研究（如 NCT01364467）對 Guaiacol 的外推可行性及其限制
- 確認 Guaiacol 在目標劑型（如吸入、含漱液）的人體安全劑量範圍
- 取得原廠仿單或相關國家藥品監管機構的警語與禁忌資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

