---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Albutrepenonacog Alfa：從血友病 B 到偽性馮威里氏病

## 一句話總結

Albutrepenonacog alfa 是一種長效型重組凝血因子 IX 白蛋白融合蛋白（rIX-FP），原本用於 **B 型血友病**（先天性凝血因子 IX 缺乏症）的預防與治療。
TxGNN 模型預測它可能對**偽性馮威里氏病 (Pseudo-von Willebrand Disease)** 等 6 種出血性疾病有效，
然而所有預測適應症均**無臨床試驗或文獻支持（L5）**，且機轉分析顯示多數適應症與藥物作用機轉存在根本性不符。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | B 型血友病（先天性凝血因子 IX 缺乏症） |
| 預測新適應症 | 偽性馮威里氏病 (Pseudo-von Willebrand Disease) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

**藥物機轉背景**：Albutrepenonacog alfa（品牌名：Idelvion）是重組人類凝血因子 IX（rFIX）與人類血清白蛋白的融合蛋白，透過白蛋白融合技術將半衰期延長至約 102 小時（每 7–14 天注射一次）。其作用屬於**二級止血**（凝血因子級聯）：補充缺乏的 FIX，使內源性凝血途徑恢復正常，最終生成凝血酶並形成穩定纖維蛋白凝塊。

**預測的機轉挑戰**：偽性馮威里氏病的致病機轉為血小板 GPIb 的功能增益突變（gain-of-function），導致血小板與 vWF 過度結合而提早被清除，屬**一級止血**（血小板）缺陷。凝血因子 IX 作用於凝血因子級聯，對血小板數量、功能或 GPIb/vWF 的互動無任何直接影響，兩者機轉無直接關聯。

**TxGNN 預測侷限性**：高預測分數主要反映知識圖譜中「出血性疾病」節點的空間鄰近性，而非真實的治療關聯。圖神經網路可辨識疾病類群相似性，但無法自動區辨一級止血（血小板）與二級止血（凝血因子）的根本機轉差異，此為本批預測需謹慎解讀的關鍵原因。

---

## 所有預測適應症概覽

本次 Evidence Pack 共包含 6 個預測適應症，所有適應症均為 **L5 證據等級**，機轉適配性分析摘要如下：

| 排名 | 疾病名稱 | TxGNN 分數 | 機轉適配性 | 建議 |
|------|---------|-----------|-----------|------|
| 1 | 偽性馮威里氏病 (Pseudo-von Willebrand Disease) | 99.94% | ❌ 不符（一級 vs 二級止血機轉差異） | Hold |
| 2 | 血小板初級釋放障礙 (Primary Release Disorder of Platelets) | 99.94% | ❌ 不符（顆粒釋放缺陷，FIX 無干預機制） | Hold |
| 3 | Glanzmann 血小板功能不全症 (Glanzmann Thrombasthenia) | 99.92% | ⚠️ 極有限（rFVIIa 有旁路案例，但 rFIX 無對應證據） | Hold |
| 4 | Scott 症候群 (Scott Syndrome) | 99.63% | ⚠️ 最弱理論合理性（PS 外翻缺陷可能影響 tenase 組裝），但無任何研究支持 | Hold |
| 5 | 膠原蛋白受體缺陷出血傾向 (Bleeding Diathesis due to Collagen Receptor Defect) | 99.28% | ❌ 不符（血小板-膠原蛋白黏附障礙，FIX 無干預機制） | Hold |
| 6 | 先天性血小板減少症出血障礙 (Hemorrhagic Disorder due to Constitutional Thrombocytopenia) | 99.26% | ❌ 不符（血小板數量問題，補充 FIX 對生成無影響） | Hold |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

針對上述 6 個預測適應症（偽性馮威里氏病、血小板初級釋放障礙、Glanzmann 血小板功能不全症、Scott 症候群、膠原蛋白受體缺陷出血傾向、先天性血小板減少症出血障礙），經查詢 ClinicalTrials.gov 及 ICTRP，均未檢索到任何相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

經查詢 PubMed，上述所有預測適應症與 Albutrepenonacog alfa 的組合均無相關文獻記錄。

---

## 台灣上市資訊

Albutrepenonacog alfa 目前在台灣**尚未取得藥品許可證**，無任何上市記錄。

> 備註：該藥物在歐盟（EMA 核准，品牌名 Idelvion）及美國（FDA 核准）已核准用於 B 型血友病成人及兒童患者，但台灣藥政主管機關（衛福部食藥署，TFDA）目前無相關許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單（Idelvion® Prescribing Information）。

> **資料缺口說明**：本 Evidence Pack 尚未收到 TFDA 仿單警語/禁忌（DG001，Blocking 級別），以及詳細作用機轉資料（DG002，High 級別）。在補充上述資料前，無法完成 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
所有 6 個預測適應症均僅有 L5 等級的模型預測，**完全無臨床試驗或文獻支持**。更關鍵的是，機轉分析顯示這些預測目標疾病（均為一級止血/血小板功能疾病）與 Albutrepenonacog alfa 的作用位點（二級止血/凝血因子 IX）存在**根本性的機轉不符**，TxGNN 的高分主要反映出血性疾病節點的圖譜鄰近性，不代表實際治療潛力。

**若要推進需要：**
- 補充 TFDA 仿單 PDF，解析完整警語與禁忌（DG001 修復）
- 查詢 DrugBank API 取得詳細 MOA 資料（DG002 修復）
- 若考慮深入評估 Glanzmann 血小板功能不全症或 Scott 症候群（機轉上有最弱理論合理性），應先檢索相關臨床前研究，並諮詢血液科/止血專科醫師
- 建議重新評估 TxGNN 知識圖譜的訓練資料，確認「出血性疾病」節點的邊定義是否需要加入止血機轉分層（一級 vs 二級），以提升未來預測的機轉特異性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

