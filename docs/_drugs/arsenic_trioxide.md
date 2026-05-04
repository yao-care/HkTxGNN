---
layout: default
title: Arsenic Trioxide
parent: 高證據等級 (L1-L2)
nav_order: 61
evidence_level: L2
indication_count: 10
---

# Arsenic Trioxide
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

# Arsenic Trioxide（三氧化二砷）：從急性前骨髓性白血病到骨髓增生異常症候群

---

## 一句話總結

Arsenic Trioxide（三氧化二砷，ATO）是經 FDA 核准用於復發性／難治性急性前骨髓性白血病（APL）的抗腫瘤藥物，以其獨特的 PML-RARα 融合蛋白降解機轉聞名。TxGNN 模型預測它可能對**骨髓增生異常症候群（Myelodysplastic Syndrome, MDS）** 有效，預測分數高達 **99.91%**（Rank 6；MDS 各亞型預測分數均在 Rank 1–6 之間，最高達 99.93%）。目前有 **超過 20 項臨床試驗**及 **20 篇文獻**（含 2023 年系統性回顧與網路 meta 分析）支持此方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性前骨髓性白血病（APL，復發／難治性） |
| 預測新適應症 | 骨髓增生異常症候群（Myelodysplastic Syndrome, MDS） |
| TxGNN 預測分數 | 99.91%（MDS 廣義；MDS 亞型最高 99.93%） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

ATO 在 APL 中的作用機轉已被充分闡明：ATO 與 PML-RARα 融合蛋白的 PML 部分直接結合，誘導其多聚素化與蛋白酶體降解，進而促進白血病細胞分化與凋亡。此外，ATO 透過累積活性氧（ROS）、抑制 NF-κB 訊號通路、調節 BCL-2 家族蛋白（下調 BCL-2、FLIP），以多重途徑驅動血液腫瘤細胞死亡。

MDS 與 APL 同屬骨髓造血異常疾病，均以無效造血（ineffective hematopoiesis）及克隆性造血幹細胞病變為核心特徵。MDS 細胞中同樣存在 NF-κB 過度活化（尤其是高危亞型 RAEB），而 ATO 的 NF-κB 抑制及 FLIP 下調機轉（PMID 16105982）已在 MDS 骨髓單核細胞中獲得直接實驗支持（PMID 22964015）。此外，ATO 與去甲基化藥物（Decitabine、Azacitidine）的協同凋亡作用——透過內質網壓力及表觀遺傳調控——進一步強化了組合療法的機轉合理性（PMID 30898879）。

在臨床層面，多項 Phase 2 試驗已完成，2023 年系統性回顧與網路 meta 分析（PMID 37908176）系統性確認 ATO 含藥方案在 MDS 具統計學意義療效，單藥有效率約 20%，組合療法（尤其是 ATO + Decitabine）表現更佳。目前更有 2 項主動招募中的試驗（NCT06670222、NCT06778187）探索口服 ATO（Arsenol®）新劑型，代表本領域具持續研究動能。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06670222](https://clinicaltrials.gov/study/NCT06670222) | Phase 1 | 招募中 | 24 | 口服 ATO 劑量遞增於低危 MDS（ESA 及 Luspatercept 治療失敗後），評估新給藥途徑安全性（2025 年開始） |
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | 招募中 | 30 | 口服 ATO（Arsenol®）+ 低強度療法於未治療或復發 TP53 突變 MDS／AML，代表口服劑型新方向（2025 年開始） |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | 完成 | 92 | 隨機分組試驗：Decitabine vs. Decitabine + Carboplatin vs. Decitabine + ATO 於復發/難治/老年 AML 及 MDS，直接比較療效 |
| [NCT00274781](https://clinicaltrials.gov/study/NCT00274781) | Phase 2 | 完成 | 30 | ATO + Gemtuzumab Ozogamicin（Mylotarg）於晚期 MDS，直接對應適應症，提供組合療效與安全性資料 |
| [NCT00195104](https://clinicaltrials.gov/study/NCT00195104) | Phase 1/2 | 完成 | 87 | ATO + 低劑量 Cytarabine 於高危 MDS 及不良預後 AML，CR 率 17%，4 週死亡率 8% |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | 完成 | 13 | IV Decitabine + ATO + Ascorbic Acid 劑量探索於 MDS／AML，確立三藥組合安全性基礎 |
| [NCT00621023](https://clinicaltrials.gov/study/NCT00621023) | Phase 2 | 完成 | 7 | Decitabine + ATO + Ascorbic Acid 於 MDS，初步探索三藥協同安全性 |
| [NCT00274820](https://clinicaltrials.gov/study/NCT00274820) | Phase 2 | 完成 | 15 | TADA 方案（Thalidomide + ATO + Dexamethasone + Ascorbic Acid）於 MDS／骨髓纖維化重疊疾病 |
| [NCT00803530](https://clinicaltrials.gov/study/NCT00803530) | Phase 2 | 終止 | 55 | ATO + Ascorbic Acid 於 MDS，多中心前瞻性試驗，樣本數為同類試驗最大，提前終止原因需進一步查閱 |
| [NCT00251511](https://clinicaltrials.gov/study/NCT00251511) | Phase 2 | 終止 | 60 | ATO + Thalidomide 於低、中危及高危 MDS（IPSS 分層），提供多風險群組合耐受性資訊 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | 系統性回顧／網路 Meta 分析 | Hematology | 系統性評估 ATO 含藥方案在 MDS 的療效與不良事件，探索最佳組合（最高等級證據） |
| [40167011](https://pubmed.ncbi.nlm.nih.gov/40167011/) | 2025 | 臨床回溯試驗 | Hematology | Decitabine + ATO 於老年高危 MDS 患者的療效與安全性，提供近期真實世界資料 |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | 臨床比較研究 | Immunopharmacol Immunotoxicol | 口服（雄黃）vs. 靜脈注射 ATO 於 MDS 鼠模型的免疫學變化比較，支持口服劑型開發 |
| [18282365](https://pubmed.ncbi.nlm.nih.gov/18282365/) | 2007 | 綜述 | Clin Lymphoma Myeloma | ATO 在白血病及 MDS 的最新資料彙整，包含緩解率與分子反應率分析 |
| [20425329](https://pubmed.ncbi.nlm.nih.gov/20425329/) | 2006 | 綜述 | Curr Hematol Malig Rep | ATO 在 MDS 的多重機轉（促凋亡、抗增殖、抗血管生成）與臨床應用回顧，單藥有效率約 20% |
| [30898879](https://pubmed.ncbi.nlm.nih.gov/30898879/) | 2019 | 前臨床 | J Investig Med | Decitabine + ATO 協同透過內質網壓力誘導 MDS 細胞凋亡（MUTZ-1 及 SKM-1 細胞株）|
| [22964015](https://pubmed.ncbi.nlm.nih.gov/22964015/) | 2012 | 臨床／分子研究 | J Hematol Oncol | ATO + Ascorbic Acid 對 MDS 患者 BCL2 家族基因表現的體內影響，93 個凋亡相關基因分析 |
| [16105982](https://pubmed.ncbi.nlm.nih.gov/16105982/) | 2005 | 機轉研究 | Blood | ATO 誘導 MDS 細胞凋亡的 NF-κB 及 FLIP 機轉，低危 vs. 高危亞型存在差異 |
| [15610661](https://pubmed.ncbi.nlm.nih.gov/15610661/) | 2005 | 綜述 | Curr Hematol Rep | ATO 在 MDS 的臨床應用回顧：機轉、單藥及組合療法療效摘要 |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase 1/2 試驗 | Leukemia Res | ATO + 低劑量 Cytarabine 於中高危 MDS（n=49），CR 率 17%，耐受性可接受 |

---

## 細胞毒性

Arsenic Trioxide 屬抗腫瘤藥物，具傳統細胞毒性與分化誘導雙重機轉，須評估以下風險：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗腫瘤藥物（分化誘導劑 + 細胞凋亡誘導劑，非傳統烷化劑或核苷類似物） |
| 骨髓抑制風險 | 中度（可能出現嗜中性球減少、血小板減少；MDS 患者本身已有血球減少，疊加風險更高） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類計數）、肝腎功能、電解質（K⁺、Mg²⁺ 需維持正常範圍）、**心電圖（QTc 間期，每週監測）** |
| 特殊毒性警示 | **QT 延長**（重要黑框警告）：需避免與其他 QT 延長藥物合用；砷蓄積及周圍神經病變（長期使用）；APL 分化症候群（APL 適應症相關，MDS 中較罕見） |
| 處置防護 | 需依細胞毒性藥物安全處置規範操作；靜脈製劑須稀釋（100–250 mL 5% G/S）後緩慢滴注（1–2 小時） |

---

## 安全性考量

**主要警示（基於藥物特性）：**

- **QT 延長**：ATO 為已知 QT 延長藥物，使用前需確認基礎 QTc < 500 ms，並維持電解質（K⁺、Mg²⁺）在正常範圍。同時使用其他 QT 延長藥物（如某些抗心律不整藥、抗生素）須特別謹慎。
- **砷蓄積與神經毒性**：長期使用可能累積，需監測周圍神經病變症狀。
- **MDS 患者特殊考量**：MDS 患者本身常有血球減少及器官功能受損，使用 ATO 時毒性風險可能高於 APL 患者，劑量及療程調整需個別化評估。

完整仿單警語、禁忌症及藥物交互作用資訊請參考原廠仿單（Trisenox® 或相應製劑）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
2023 年系統性回顧及網路 meta 分析（PMID 37908176）系統性確認 ATO 含藥方案於 MDS 具療效，多項 Phase 2 試驗（含 2 項正在招募的口服 ATO 試驗）顯示本領域研究動能持續旺盛。機轉關聯性充分（NF-κB 抑制、BCL-2 家族調節、與去甲基化藥物的表觀遺傳協同），屬 APL 至 MDS 的合理疾病譜延伸。惟 ATO 在香港目前無上市許可，且 MDS 中的確效療效與 APL 相比尚顯不足，需設立明確安全監測防護措施。

**若要推進需要：**
- 向香港衛生署（Department of Health）申請特殊用藥許可或研究性用藥（investigational use）資格
- 取得完整仿單，審閱 QT 延長、骨髓抑制等黑框警告與禁忌症（資料缺口 DG001）
- 確認 MDS 亞型及 IPSS 風險分層，選擇最適合的組合療法方案（如低危：單藥或 ATO + Ascorbic Acid；高危：DAC + ATO）
- 建立基礎心電圖評估及電解質監測方案作為用藥前篩選標準
- 追蹤 NCT06670222 及 NCT06778187 兩項口服 ATO 試驗結果，評估口服製劑可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

