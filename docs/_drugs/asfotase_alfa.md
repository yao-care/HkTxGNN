---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Asfotase alfa：從低磷酸酶症到粒線體氧化磷酸化障礙

## 一句話總結

Asfotase alfa（Strensiq）是一種重組組織非特異性鹼性磷酸酶（TNSALP）酵素替代療法，原本用於治療低磷酸酶症（Hypophosphatasia, HPP）這種罕見遺傳性代謝疾病。
TxGNN 模型預測它可能對**核 DNA 異常粒線體氧化磷酸化障礙（Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies）** 有效，
然而目前**尚無任何臨床試驗或文獻**支持此方向，證據等級為最低階（L5），建議暫緩。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 低磷酸酶症（Hypophosphatasia, HPP） |
| 預測新適應症 | 核 DNA 異常粒線體氧化磷酸化障礙 |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Asfotase alfa 是針對低磷酸酶症（HPP）設計的酵素替代療法——HPP 係因 *ALPL* 基因突變導致 TNSALP 酵素缺乏，使得無機焦磷酸（PPi）在骨骼局部過度累積，阻礙骨礦化並引發骨折、骨痛及多系統病變。Asfotase alfa 透過補充重組 TNSALP 來降解過量 PPi，其分子設計含 C 端十個天門冬胺酸序列（D10），使酵素能主動靶向骨骼礦化位點。

TxGNN 模型預測的機轉連結在於：TNSALP 參與嘌呤核苷酸循環（purine nucleotide cycle），PPi 的累積在理論上可能干擾粒線體 ATP 合成路徑，因此推測 Asfotase alfa 可能影響粒線體氧化磷酸化功能。

然而，此連結屬**高度間接推論**，目前完全缺乏體外、動物或臨床依據。TxGNN 的高預測分數較可能來自知識圖譜中兩者共享的「罕見代謝疾病」或「ATP／能量代謝」節點，而非代表真實生物路徑的直接對應。整體機轉合理性偏低。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Asfotase alfa 目前**未在香港上市**，無任何已核准藥物許可證。如有臨床需求，可能需透過恩慈用藥（compassionate use）或特殊藥物進口途徑申請。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有 10 個 TxGNN 預測適應症均為 L5 等級，完全缺乏臨床試驗與文獻支持，無法進入安全性初評（S0 階段）。
- 排名第一的預測（粒線體氧化磷酸化障礙）機轉連結屬高度間接推論，生物合理性不足，難以支撐再利用開發決策。

**若要推進任何預測方向，需要：**
- **補充 MOA 資料**：查詢 DrugBank API（DB09105）或解析 EMA/FDA 原廠仿單，釐清完整作用機轉
- **補充安全性資料**：解析仿單 PDF，取得主要警語、禁忌症及藥物交互作用
- **評估機轉較相關的適應症**：Rank 10（cystinosis）和 Rank 6（lysosomal storage disease with skeletal involvement）在機轉上與 TNSALP／骨礦化缺陷的連結相對最強，建議優先做文獻回顧與 biomarker 分析（血/尿 PPi、PLP 水準）
- **確認香港引進可行性**：評估孤兒藥申請途徑及健保/藥事法規現況
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

