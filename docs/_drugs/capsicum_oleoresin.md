---
layout: default
title: Capsicum Oleoresin
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Capsicum Oleoresin
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

# Capsicum oleoresin：從外用止痛劑到周邊運動神經病變-自律神經失調症候群

## 一句話總結

Capsicum oleoresin（辣椒油樹脂）是辣椒素（capsaicin）的天然萃取物，傳統上作為外用刺激性止痛劑使用，目前在香港無核准上市紀錄。TxGNN 模型預測它可能與**周邊運動神經病變-自律神經失調症候群 (peripheral motor neuropathy-dysautonomia syndrome)** 有關聯，然而此預測排名極低（第 2,403,479 名），目前**無任何臨床試驗或文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准適應症資料（香港未上市） |
| 預測新適應症 | 周邊運動神經病變-自律神經失調症候群 |
| TxGNN 預測分數 | 50.00%（模型排名第 2,403,479） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理學背景知識，Capsicum oleoresin 的活性成分為辣椒素（capsaicin），主要透過激活並脫敏感覺神經末梢的 **TRPV1（暫態受器電位香草素 1 型）離子通道**發揮作用，造成局部 P 物質耗竭，進而產生止痛與抗發炎效果。

然而，此預測的機轉關聯性極弱。周邊運動神經病變-自律神經失調症候群主要涉及**運動神經元**與**自律神經系統**的功能失調，而 capsaicin 的 TRPV1 機轉作用於**傳入（感覺）神經**，對運動神經元或自律神經節的影響十分有限。雖然 TRPV1 受體在自律神經節有少量表現，但尚無直接干預運動神經病變的證據。

此外，TxGNN 模型排名第 2,403,479，預測分數僅達閾值（0.5），屬於模型可信度最低區間。這 10 個預測適應症均為罕見遺傳性症候群，且機轉評估均為「無關聯性」或「極低」，推測係模型的雜訊輸出，而非真實再利用訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Capsicum oleoresin 在香港目前無核准藥品許可證，未上市。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 模型排名極低（第 2,403,479），預測分數僅達最低閾值，且針對所有 10 個預測適應症均無臨床試驗或文獻佐證，機轉分析亦顯示 capsaicin 的 TRPV1 機轉與預測的遺傳性罕見症候群之間無合理關聯路徑。

**若要重新評估需要：**
- 從 DrugBank API 補充完整 MOA 資料與已核准適應症，確認是否有其他高分預測適應症遭遺漏
- 確認是否存在以「capsaicin」或「capsicum」為搜尋詞的更廣泛證據（本次僅查詢 Capsicum oleoresin）
- 評估是否有其他國家已核准適應症，作為潛在再利用方向的起點
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

