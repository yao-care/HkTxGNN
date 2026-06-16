---
layout: default
title: Ganirelix
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 5
---

# Ganirelix
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

# Ganirelix：GnRH 拮抗劑老藥新用預測評估

## 一句話總結

Ganirelix 為 GnRH 拮抗劑，透過阻斷 GnRH 受體抑制 LH 分泌（原核准適應症資料未收錄於本 Evidence Pack）。
TxGNN 模型預測其最高可能對**多毛症 (Hypertrichosis)** 有效，預測分數高達 **99.98%**；
然而，**全部 5 個預測適應症均為 L5 等級，無任何臨床試驗或相關文獻支持**，且機轉分析顯示多數預測為知識圖譜節點聚類所導致的系統性誤判。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未收錄（需補充，Data Gap DG001/DG002） |
| 預測新適應症（Rank 1） | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Data Gap DG002）。根據 Evidence Pack 記載的推論路徑，Ganirelix 作為 GnRH 拮抗劑，其理論機轉為：**GnRH 拮抗 → LH↓ → 睪固酮↓ → 毛囊雄性素刺激減少**，TxGNN 透過此路徑將其連結至多毛相關疾病。

然而，此預測存在根本性概念錯誤：**多毛症（hypertrichosis）與雄性素性多毛（hirsutism）是完全不同的疾病實體**。Hypertrichosis 並非由雄性素驅動，其成因包含先天遺傳、藥物誘發、代謝異常等多種機轉，GnRH 拮抗劑的降雄性素路徑對此缺乏生物學合理性。

即便 GnRH 拮抗劑在 hirsutism（雄性素性多毛）具有理論基礎，對 hypertrichosis 亦無適用依據。此預測被評定為知識圖譜中「hair growth」節點過度泛化連結所產生的誤判（graph artifact）。

---

## 全部預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | KG Rank | 證據等級 | 決策 | 機轉評估 |
|------|--------|-----------|---------|---------|------|---------|
| 1 | Hypertrichosis (disease) | 99.98% | 746 | L5 | Hold | ❌ 疾病分類錯誤，非雄性素驅動，機轉不適用 |
| 2 | Ambras type hypertrichosis universalis congenita | 99.98% | 887 | L5 | Hold | ❌ 第 8 號染色體結構重排之先天遺傳病，KG 圖噪訊 |
| 3 | Malformation syndrome with odontal/periodontal component | 99.97% | 995 | L5 | Hold | ❌ 先天結構缺陷，20 篇文獻均為牙周通論，無 drug-specific 相關性 |
| 4 | Syndrome with Dandy-Walker malformation | 99.97% | 1031 | L5 | Hold | ❌ 胚胎期後腦發育異常，先天腦部結構缺陷，無理論治療機轉 |
| 5 | Isolated genetic hair shaft abnormality | 99.97% | 1052 | L5 | Hold | ❌ 角蛋白基因突變之蛋白質結構缺陷，KG「hair」節點聚類誤判 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

所有 5 個預測適應症均未發現任何 ClinicalTrials.gov 或 ICTRP 登記試驗。

---

## 文獻證據

針對 Rank 1 適應症（多毛症），目前無相關文獻。

> **附註（Rank 3 適應症）**：Evidence Pack 在「malformation syndrome with odontal/periodontal component」搜尋到 20 篇 PubMed 文獻，但**全部為牙周疾病之通論背景文獻（如牙周炎治療指引、牙周與糖尿病關聯、牙周手術技術等），無任何文獻研究 Ganirelix 用於此適應症**。此為系統廣義搜尋所收錄的非 drug-specific 文獻，不具老藥新用相關性，判定為文獻計數誤判。

---

## 香港上市資訊

Ganirelix 目前**未在香港取得任何上市許可**，無相關許可證資料可供查詢。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
全部 5 個 TxGNN 預測適應症均為 L5 等級（僅模型預測），且機轉分析顯示預測具根本性缺陷——目標疾病均屬先天性遺傳缺陷或腦部／牙周結構異常，與 GnRH 拮抗劑的激素調控機轉無關。本批預測結果被判定為知識圖譜圖節點聚類誤判（graph artifacts），整體再利用可行性極低。

**若要重新評估或推進需要：**
- 補充 Ganirelix 原核准適應症資料及完整 MOA（Data Gap DG002）
- 補充香港或原廠仿單安全性警語及禁忌症（Data Gap DG001）
- 建議重新設定預測目標方向：Ganirelix 若有再利用潛力，應聚焦於其已知 GnRH 拮抗機轉的合理延伸領域（如子宮內膜異位症、前列腺癌輔助治療、多囊卵巢症候群等雄性素依賴性疾病），而非本次 KG 預測所生成的先天結構異常族群
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

