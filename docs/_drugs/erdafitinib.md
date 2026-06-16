---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Erdafitinib
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

# Erdafitinib：從 FGFR 突變相關腫瘤 到 肺動脈高壓

## 一句話總結

Erdafitinib 是一種泛 FGFR（纖維母細胞生長因子受體 1–4）小分子激酶抑制劑，原本用於具有 FGFR 基因變異的腫瘤治療。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，
然而目前**無臨床試驗**及**無文獻**直接支持 Erdafitinib 用於此適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 缺乏正式資料（背景已知為 FGFR 突變相關腫瘤） |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.38% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 欄位未收集完整）。根據現有背景知識，Erdafitinib 是一種泛 FGFR（FGFR1–4）選擇性小分子激酶抑制劑，透過競爭性阻斷 ATP 結合位點、抑制 FGFR 下游 MAPK 與 PI3K/AKT 訊號傳導而發揮療效，原核准適應症為具有 FGFR2/3 基因變異的尿路上皮癌。

在機轉關聯性方面，FGFR1 已被發現在肺動脈高壓（PAH）患者的肺血管床中呈顯著上調表現；FGF/FGFR 訊號參與肺動脈平滑肌細胞（PASMC）的異常增殖、抗凋亡及血管重塑，與 PAH 的核心病生理高度重疊。多項預臨床研究顯示 FGFR 抑制在 PAH 動物模型中具有潛在療效。

然而，Erdafitinib 本身迄今無任何 PAH 相關人體試驗發表。TxGNN 高分（99.38%）反映的是知識圖譜中 FGFR 訊號節點與 PAH 疾病本體的拓撲連結度，並不等同於臨床可行性。此外，FGFR 抑制劑已知的特殊毒性（高磷血症、眼毒性、皮膚乾燥）在 PAH 患者族群（通常合併右心衰竭）中的耐受性與藥物交互作用仍完全未知，需審慎評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無 Erdafitinib 用於肺動脈高壓的相關文獻。

---

## 香港上市資訊

Erdafitinib 目前在香港未取得任何藥品上市許可，無相關許可證登記資料。

---

## 細胞毒性

Erdafitinib 為抗腫瘤標靶藥物（FGFR 激酶抑制劑），以下為細胞毒性相關參考資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（泛 FGFR 小分子激酶抑制劑） |
| 骨髓抑制風險 | 低至中度（較傳統化療輕，仍可能出現貧血、嗜中性白血球減少） |
| 致吐性分級 | 低度 |
| 監測項目 | 血磷（高磷血症為最常見毒性）、眼科檢查（中心視網膜靜脈阻塞/中心性漿液性視網膜病變）、CBC、肝腎功能 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Erdafitinib 用於肺動脈高壓目前完全缺乏臨床試驗與直接文獻支持（L5 等級），加上香港尚未上市、藥物安全性資料缺口均為阻斷性問題（Blocking），現階段無法進入正式安全性評估。雖然 FGFR 訊號在 PAH 病生理中具一定機轉合理性，但僅憑模型預測分數不足以支撐再利用決策。

**若要推進需要：**
- 補充完整的藥物 MOA 與安全性資料（原廠仿單 PDF 解析、DrugBank API 查詢）
- 搜尋泛 FGFR 抑制劑類別（不限 Erdafitinib）用於 PAH 的預臨床及早期臨床文獻，確認類效應（class effect）可能性
- 評估 PAH 患者族群（右心衰竭合併症）對 FGFR 抑制劑毒性的耐受性
- 確認香港藥物申請策略（是否需先取得其他主要市場 PAH 適應症核准）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

