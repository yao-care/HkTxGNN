---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 5
---

# Flurbiprofen
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

# Flurbiprofen：從抗炎鎮痛到罕見骨骼發育疾病

## 一句話總結

Flurbiprofen 是一種 COX-1/COX-2 抑制劑（NSAID），臨床上用於抗炎與鎮痛，眼科製劑亦用於術後炎症控制。TxGNN 模型預測其可能對**肢端中段肢骨發育不良 Hunter-Thompson 型（acromesomelic dysplasia, Hunter-Thompson type）**等 5 項罕見骨骼發育疾病有效，但目前**無任何臨床試驗或文獻**支持上述任一預測，全數屬模型推論結果（L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗炎鎮痛（COX-1/COX-2 抑制劑，NSAID 類） |
| 預測新適應症（Rank 1） | 肢端中段肢骨發育不良 Hunter-Thompson 型 (acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Data Gap）。根據已知資訊，Flurbiprofen 屬非類固醇抗炎藥（NSAID），透過抑制 COX-1/COX-2 酶降低前列腺素合成，發揮抗炎、鎮痛及退熱作用；眼科製劑形式亦用於白內障手術術後炎症控制。

TxGNN 本次預測的 **5 項適應症**均屬罕見先天性骨骼或結締組織疾病，其機轉連結概述如下：

| Rank | 疾病 | 主要致病路徑 | 與 COX 抑制的機轉關聯 |
|------|------|-------------|----------------------|
| 1 | 肢端中段肢骨發育不良 Hunter-Thompson 型 | CDMP1/GDF5 基因突變→骨骼發育缺損 | 極薄弱：前列腺素參與骨代謝，但對 GDF5 信號通路無直接作用 |
| 2 | 短指並指症候群 | HOXD/GJA1 等基因突變→胚胎期結構缺損 | 無：胚胎發育期缺損無法以 COX 抑制修復 |
| 3 | 脈絡膜缺損性小眼症合併根節段性肢體發育不全 | 胚胎眼球及肢體發育相關基因異常 | 極薄弱：眼科製劑可抗術後炎症，但無法修正基因層次結構缺損 |
| 4 | 短椎體-釉質發育不全症候群 | 膠原或釉質蛋白基因異常 | 無：長期 COX 抑制甚至可能不利軟骨代謝 |
| 5 | 肌硬化症 | TGF-β 纖維化路徑→肌肉瀰漫纖維化 | 偏弱：急性炎症與纖維化早期有關，但 COX 抑制無法逆轉已建立的纖維化 |

**高分原因分析：** 上述 5 項疾病的 TxGNN 分數均高達 ≥ 99.98%，但全數缺乏臨床支撐，形成明顯落差。此模式通常反映知識圖譜中罕見病節點與 NSAID 相關節點之間的**拓撲相似性**（共享鄰居結構），而非生物學上的直接相關——屬 GNN 模型常見的假陽性情境，尤其在罕見病節點群聚時更易發生。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

（已查詢 ClinicalTrials.gov 及 ICTRP，Flurbiprofen 用於上述 5 項預測適應症均無任何登記紀錄。）

---

## 文獻證據

目前無相關文獻。

（已查詢 PubMed，Flurbiprofen 配合各預測適應症之組合均無命中結果。）

---

## 香港上市資訊

Flurbiprofen 目前在香港**未上市**，無任何有效許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
5 項預測適應症均為罕見先天性骨骼或結締組織發育疾病，致病機轉以基因缺陷為主，Flurbiprofen 的 COX 抑制機轉對此類疾病無已知直接作用路徑；且全數缺乏臨床試驗與文獻支持（L5），同時 Flurbiprofen 在香港尚未上市，整體評估不支持進一步推進。

**若要推進需要：**

- **補足資料缺口 DG001**：從 TFDA 官網下載原廠仿單 PDF，解析警語與禁忌症資料
- **補足資料缺口 DG002**：查詢 DrugBank API 取得完整作用機轉（MOA）描述
- **模型假陽性驗證**：檢視 TxGNN 知識圖譜拓撲，確認高分是否源於罕見病節點共享鄰居結構；可考慮以 Weisfeiler-Leman 圖核或 pathway enrichment 方法進行交叉驗證
- **肌硬化症（Rank 5）選擇性追蹤**：若有興趣，可單獨進行前臨床文獻搜尋，評估抗炎介入在纖維化早期是否具探索空間，但應在取得 MOA 與安全性資料後再行決策
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

