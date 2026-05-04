---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 2
---

# Baricitinib
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

# Baricitinib：從自體免疫疾病到 Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## 一句話總結

Baricitinib 是一種口服 JAK1/JAK2 抑制劑，透過阻斷 JAK-STAT 細胞激素訊號傳遞發揮抗炎作用，目前在香港尚未取得上市許可。TxGNN 模型預測它可能對**伴缺損小眼症－肢根型發育不良症候群（Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome）**有效，但目前**無任何臨床試驗或文獻**支持這個方向，屬純模型拓撲預測結果，需極度謹慎解讀。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港無上市資料（國際已核准：類風濕性關節炎、異位性皮膚炎、COVID-19） |
| 預測新適應症 | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

Baricitinib 是選擇性 JAK1/JAK2 抑制劑，透過阻斷 JAK-STAT 細胞激素訊號傳遞，抑制多種促炎細胞激素（如 IL-6、IFN-γ、IL-2）的下游效應。在國際上已核准用於中至重度類風濕性關節炎、異位性皮膚炎，及 COVID-19 相關重症。其核心機轉為免疫調節，而非直接的細胞增殖或發育調控。

Colobomatous microphthalmia-rhizomelic dysplasia syndrome 是一種**極罕見的先天性發育缺陷症候群**，主要表現為眼球缺損（coloboma）、小眼症（microphthalmia）及肢根型骨骼發育不良（rhizomelic dysplasia），發病機轉主要與 PAX2、SHH、STRA6 等胚胎發育調控途徑的基因異常相關，屬遺傳性先天缺陷，並非後天炎症或免疫驅動疾病。

目前兩者之間的機轉連結**高度間接且缺乏實驗依據**：JAK-STAT 訊號雖在早期胚胎發育中透過細胞激素調控扮演輔助角色，但現無任何臨床前研究或臨床資料直接支持 JAK 抑制與此症候群的治療關聯。TxGNN 高分（0.9994）反映的是知識圖譜中**節點拓撲相似性**，而非生物學驗證，應視為探索性假設，而非臨床預測訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單（Olumiant® 仿單，Eli Lilly）。

---

## 結論與下一步

**決策：Hold**

**理由：**
此預測適應症為極罕見的先天性遺傳發育缺陷，其病理機轉（胚胎期發育基因異常）與 Baricitinib 的核心藥理機轉（成人免疫調節）存在根本性差距，且目前完全無臨床試驗、文獻或臨床前資料支持，證據等級僅為 L5（純模型預測），建議維持 Hold，不進入下一階段評估。

**若要推進需要：**
- **基礎研究確認**：文獻搜尋是否有 JAK-STAT 在 PAX2/SHH/STRA6 發育通路中直接作用的基礎研究
- **臨床前驗證**：細胞或斑馬魚/小鼠模型中驗證 JAK 抑制對眼球/骨骼發育的影響
- **孤兒藥可行性評估**：此症候群極罕見，需評估患者族群規模及商業可行性
- **安全性資料補充**：取得 TFDA/香港衛生署仿單，補充完整警語、禁忌症及 MOA 資料
- **香港藥監登記評估**：確認 Baricitinib 在香港未上市的監管路徑
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

