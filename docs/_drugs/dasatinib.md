---
layout: default
title: Dasatinib
parent: 高證據等級 (L1-L2)
nav_order: 179
evidence_level: L2
indication_count: 10
---

# Dasatinib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Dasatinib：從骨髓性白血病到 Ewing 肉瘤

## 一句話總結

Dasatinib 是廣泛應用於骨髓性白血病的第二代酪胺酸激酶抑制劑（TKI），透過抑制 BCR-ABL 及 Src 家族激酶發揮療效。TxGNN 模型預測它可能對 **Ewing 肉瘤（Ewing Sarcoma）** 有效，目前有 **3 個臨床試驗**和 **9 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性骨髓性白血病（CML）及費城染色體陽性急性白血病（全球核准；香港暫未上市） |
| 預測新適應症 | Ewing 肉瘤（Ewing Sarcoma） |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Dasatinib 是多靶點口服 TKI，主要抑制 BCR-ABL、**Src 家族激酶（SFK）**、c-KIT 及 PDGFR-β，其中對 Src 的奈莫爾（nM）級別抑制活性是連結 Ewing 肉瘤的核心機轉。目前官方 MOA 備案資料缺乏，以下分析基於已發表文獻。

Ewing 肉瘤由特徵性 **EWS-FLI1 融合蛋白**驅動，該融合蛋白會上調 Src 訊號活化，促進腫瘤細胞侵襲、遷移及 invadopodia（侵襲偽足）形成。腫瘤微環境壓力（低氧、低養分）可進一步透過 **Tenascin C–Src 軸**誘發侵略性表型。Dasatinib 透過抑制 **FAK-Src 複合體**，理論上可阻斷這些轉移促進機轉，在 c-KIT 及 PDGFR 過表達的 Ewing 肉瘤細胞中具雙重靶向優勢。

多項體外研究已直接驗證 Dasatinib 在 Ewing 肉瘤細胞株的抗增殖與抗遷移活性；大型 Phase 2 試驗（366 人）亦涵蓋 Ewing 肉瘤亞型。然而，Dasatinib 單藥在廣泛性肉瘤 Phase 2 中未達顯著療效，提示未來應考慮組合策略或生物標記導向的病人選擇。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | 完成 | 366 | Dasatinib 用於晚期肉瘤，評估反應率及 6 個月無進展存活率；涵蓋多種亞型（可能含 Ewing 亞組），缺乏 Ewing 專屬分析，需聯繫試驗主持人取得亞組數據 |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | 提前終止 | 7 | Dasatinib 合併 Ifosfamide／Carboplatin／Etoposide 用於兒科肉瘤（含 Ewing 適應症），因提前終止且入組人數極少，無法提供療效結論 |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | 招募中 | 41 | B7-H3 CAR-T 細胞用於復發／難治性實體瘤（含 Ewing），為免疫治療試驗，與 Dasatinib 直接再利用相關性低 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Src 在肉瘤腫瘤生物學中的角色綜述，討論 Src 靶向治療（含 Dasatinib）在肉瘤的可行性與臨床意義 |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | 轉化研究 | Sarcoma | FAK-Src 複合體在 Ewing 肉瘤、DSRCT 及橫紋肌肉瘤的靶向治療探討；Dasatinib 單藥 Phase 2 未成功，組合靶向策略仍具潛力 |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | 體外實驗 | Oncology Reports | Dasatinib 在 Ewing 肉瘤及神經母細胞瘤細胞株中直接展現抗增殖與抗遷移活性，c-KIT 及 PDGFR 為主要靶點 |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | 體外實驗 | Cancer Research | Dasatinib 抑制多種人類肉瘤細胞株的遷移與侵襲；在依賴 SRC 存活的骨肉瘤細胞中誘導凋亡，確立 Src 靶向可行性 |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | 機轉研究 | Neoplasia | Tenascin C 與 Src 協作驅動 Ewing 肉瘤 invadopodia 形成與轉移；強化 Src 抑制作為轉移防治策略的機轉理據 |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | 機轉研究 | Neoplasia | 微環境壓力透過 Src 依賴性機轉誘導 Ewing 肉瘤細胞 invadopodia 形成與遷移，確立 Src 為轉移驅動關鍵因子 |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | 體外研究 | Cell Commun Signal | CXCR4 拮抗劑在 Ewing 肉瘤中促進受體酪胺酸激酶訊號活化，與 Dasatinib 相關訊號通路有部分交集 |

---

## 香港上市資訊

Dasatinib 目前在香港**無任何核准上市許可**（0 張許可證）。如需臨床使用，須透過個案藥物特別申請（Unregistered Drug Application）向衞生署申請，並取得醫管局藥物委員會批准。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多靶點 TKI：BCR-ABL／Src 家族激酶／c-KIT／PDGFR 抑制劑，非傳統細胞毒性化療） |
| 骨髓抑制風險 | 中度（常見嗜中性白血球減少、血小板減少、貧血，為已知臨床副作用） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC（含白血球分類）、肝腎功能、胸部 X 光（胸腔積液評估）、QTc 心電圖、血磷濃度 |
| 處置防護 | 口服製劑，依標靶藥物處置規範操作；需重點監測胸腔積液（發生率約 28–35%，為最常見嚴重副作用），長期使用者另需評估肺動脈高壓風險 |

---

## 安全性考量

安全性資訊請參考原廠仿單（Bristol-Myers Squibb，Sprycel®）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Dasatinib 抑制 Src／FAK 複合體的機轉與 Ewing 肉瘤生物學高度契合，具備直接體外活性佐證（c-KIT、PDGFR 雙重靶向）；大型完成 Phase 2 試驗（366 人）提供了安全性參考框架，整體科學基礎足以支持進一步探索。然而，單藥在肉瘤的臨床結果未如預期，建議以組合療法或生物標記導向策略為核心方向推進。

**若要推進需要：**
- 取得 NCT00464620 的 Ewing 肉瘤亞組詳細療效數據（聯繫試驗主持人或查閱未發表子研究）
- 補齊安全性備案資料（原廠仿單警語、禁忌症及藥物交互作用清單）
- 確認完整作用機轉（DrugBank MOA 資料查詢）
- 評估 Dasatinib 合併標準化療（如 ICE 方案）的組合療法設計可行性
- 在香港臨床應用前，完成衞生署未登記藥物特別申請程序
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

