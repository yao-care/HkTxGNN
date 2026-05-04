---
layout: default
title: Calcifediol
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 4
---

# Calcifediol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Calcifediol：從維生素D補充到維生素D依賴性佝僂病

> **本報告涵蓋 4 個預測適應症（多適應症評估），僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。**

---

## 一句話總結

Calcifediol（25-羥基維生素D3）是維生素D在人體循環中最主要的儲存形式，作為維生素D活化通路的關鍵中間代謝物，長期用於維生素D缺乏症的補充治療。TxGNN 模型預測它可能對**維生素D依賴性佝僂病（VDDR）**、**遺傳性低磷酸血症佝僂病**及**腎小管酸中毒**等罕見代謝骨病有效，其中 VDDR Type 1B（25-羥化酶缺陷）的機轉匹配度最高，目前有 **2 個臨床試驗**和 **17 篇文獻**支持此方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維生素D缺乏症補充（25-羥基維生素D3，全球已知臨床應用） |
| 最佳預測新適應症 | 維生素D依賴性佝僂病（vitamin D-dependent rickets） |
| TxGNN 預測分數 | 99.18%（Rank 4，最高證據等級者） |
| 證據等級 | L3（維生素D依賴性佝僂病） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails（VDDR-1B 亞型） |

---

## 多適應症預測總覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|-----------|-----------|---------|---------|
| 1 | obsolete vitamin D deficiency（廢棄術語，無效疾病碼） | 99.99% | L5 | Hold |
| 2 | 腎小管酸中毒（renal tubular acidosis） | 99.86% | L4 | Research Question |
| 3 | 遺傳性低磷酸血症佝僂病（hereditary hypophosphatemic rickets） | 99.76% | L4 | Research Question |
| 4 | 維生素D依賴性佝僂病（vitamin D-dependent rickets） | 99.18% | L3 | **Proceed with Guardrails** |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知生化特性，Calcifediol（化學名 25-羥基維生素D3，25(OH)D3）是維生素D在肝臟由 25-羥化酶（CYP2R1）催化後的中間代謝物，正常代謝流程為：維生素D3 → **25(OH)D3（calcifediol）** → 1,25(OH)2D3（calcitriol，活性形式）。它是人體血液中主要的維生素D儲存形式，藥理作用依賴於後續腎臟 CYP27B1 的活化。

TxGNN 預測的四個適應症均屬維生素D代謝或磷鈣代謝通路的疾病，這與 calcifediol 作為維生素D活化中間體的化學本質高度一致。各適應症的機轉匹配度因疾病的核心缺陷位置而顯著不同。

其中，**VDDR Type 1B**（CYP2R1突變，25-羥化酶功能缺陷）是機轉吻合度最高的亞型：患者因無法自行合成 calcifediol，直接補充 calcifediol 即可替代缺失的代謝中間物，理論上具有根治性效果。相較之下，VDDR Type 1A（CYP27B1缺陷）需要 calcitriol，VDDR Type 2A/2B（VDR突變）對任何維生素D製劑均無效，亞型分層對此適應症至關重要。

---

## 適應症四（最高證據等級）：維生素D依賴性佝僂病

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03265483](https://clinicaltrials.gov/study/NCT03265483) | NA | 已完成 | 180 | 探討鎂補充對維生素D抵抗性的影響；鎂是CYP27B1的輔因子，與VDDR機轉間接相關，屬機轉背景研究，非 calcifediol 直接療效試驗 |
| [NCT05214040](https://clinicaltrials.gov/study/NCT05214040) | N/A | 尚未招募 | 300,000 | 大規模住院患者維生素D不足盛行率觀察研究，非VDDR特定干預設計，對calcifediol療效的直接支持度低 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Review / Case Series | J Bone Miner Res | VDDR Type 1B（CYP2R1突變，25-羥化酶缺陷）臨床特徵：直接補充calcifediol可矯正缺失代謝物，是最精準的治療亞型 |
| [9316302](https://pubmed.ncbi.nlm.nih.gov/9316302/) | 1997 | Review | Acta Paediatr Jpn | VDDR I/II 型機轉與治療綜述：VDDR-I 需 1α-羥化維生素D/calcitriol，VDDR-II 受體功能障礙 |
| [2982764](https://pubmed.ncbi.nlm.nih.gov/2982764/) | 1985 | Clinical Case Series | Isr J Med Sci | 兩例 VDDR 患者診斷與治療反應：大劑量25(OH)D 可矯正 Type II 患者的鈣吸收異常 |
| [22145480](https://pubmed.ncbi.nlm.nih.gov/22145480/) | 2011 | Case Report | J Pediatr Endocrinol Metab | 非洲兒童 VDDR-I（CYP27B1缺陷）及 VDDR-II 各一例，診斷與治療困難的臨床挑戰 |
| [233695](https://pubmed.ncbi.nlm.nih.gov/233695/) | 1978 | Clinical Study | J Clin Endocrinol Metab | 對1,25(OH)2D 敏感度下降家族症候群；高劑量25(OH)D 可改善鈣吸收，提供calcifediol大劑量策略的早期依據 |
| [15972816](https://pubmed.ncbi.nlm.nih.gov/15972816/) | 2005 | Basic Science | J Biol Chem | 鑑定 CYP27B1 結合25(OH)D3 的關鍵胺基酸殘基，解析 VDDR-1A 突變的結構影響 |
| [11693961](https://pubmed.ncbi.nlm.nih.gov/11693961/) | 2001 | Review | Crit Rev Eukaryot Gene Expr | 維生素D調控成骨細胞功能與骨礦化機轉，VDDR I/II 型在骨骼鈣化的表現 |
| [26483391](https://pubmed.ncbi.nlm.nih.gov/26483391/) | 2015 | Case Series | BMJ Case Reports | 佝僂病肺部致命性呼吸道併發症，強調早期診斷與維生素D治療的緊迫性 |
| [11416220](https://pubmed.ncbi.nlm.nih.gov/11416220/) | 2001 | Basic Science | PNAS | CYP27B1 基因剔除小鼠模型：骨骼、生殖、免疫功能多重障礙，確認1α-羥化酶的全身性角色 |
| [8914979](https://pubmed.ncbi.nlm.nih.gov/8914979/) | 1996 | Ex Vivo Study | FEBS Lett | VDDR Type II 患者單核細胞對1,25(OH)2D3的細胞內鈣反應分析，提示非基因組路徑的保留 |

---

## 適應症三：遺傳性低磷酸血症佝僂病

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Narrative Review | Nutrients | 佝僂病各亞型與維生素D及類似物治療現況，包含calcifediol等代謝物的臨床定位 |
| [6976353](https://pubmed.ncbi.nlm.nih.gov/6976353/) | 1982 | Uncontrolled Clinical Trial | J Clin Endocrinol Metab | 維生素D2與磷酸補充治療X-連鎖低磷酸血症佝僂病（XLH）的療效評估 |
| [6253520](https://pubmed.ncbi.nlm.nih.gov/6253520/) | 1980 | Clinical Mechanistic Study | J Clin Invest | 評估1,25(OH)2D3在XLH發病機轉與治療中的角色，探討腎磷酸鹽丟失之外的代謝缺陷 |
| [2804451](https://pubmed.ncbi.nlm.nih.gov/2804451/) | 1989 | Physiological Study | Bone Miner | XLH患者口服磷酸負荷後維生素D代謝物的動態變化，揭示CYP27B1調控異常 |
| [20688626](https://pubmed.ncbi.nlm.nih.gov/20688626/) | 2010 | Case Report | Hormones | XLH長期治療後繼發性甲狀旁腺機能亢進，cinacalcet 介入案例 |

**機轉說明：** 遺傳性低磷酸血症佝僂病（XLH，PHEX突變）核心為FGF23過度表現，抑制腎臟CYP27B1活性並造成磷酸鹽丟失。Calcifediol可增加底物供應，理論上部分補償1,25(OH)2D3不足，但無法解除FGF23的主動抑制。現代標準治療已轉向 burosumab（抗FGF23單抗），calcifediol在此適應症為輔助角色，非首選。

---

## 適應症二：腎小管酸中毒

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11372811](https://pubmed.ncbi.nlm.nih.gov/11372811/) | 2001 | Case Report | South Med J | 四肢癱瘓患者伴發近端腎小管酸中毒與骨軟化症，維生素D缺乏為致病因素之一 |
| [3671929](https://pubmed.ncbi.nlm.nih.gov/3671929/) | 1987 | Case Report | Rev Med Bruxelles | 成人缺乏性骨軟化症合併近端小管酸中毒，描述RTA與骨骼病變的共病關係 |
| [2737043](https://pubmed.ncbi.nlm.nih.gov/2737043/) | 1989 | Methodology Study | Zhonghua Nei Ke Za Zhi | 94名健康人與98名患者血清25-OH-D3測定，骨軟化症群體顯示顯著低值 |

**機轉說明：** 腎小管酸中毒（RTA）透過持續性代謝性酸中毒促使骨骼緩衝酸負荷，造成骨質脫鈣與繼發性維生素D代謝紊亂。Calcifediol 屬對症/輔助治療（補充消耗的25(OH)D3儲量），無法修正RTA核心的小管轉運體功能障礙。目前無直接干預性臨床試驗，僅有機轉關聯案例報告。

---

## 適應症一：廢棄術語—不建議推進

排名第一的預測適應症「**obsolete vitamin D deficiency**」使用已廢棄的本體論術語（標記為 obsolete），無有效的現行疾病碼映射，無法基於廢棄術語建立再利用適應症。建議重新映射至現行術語（如 ICD-10 E55.9 Vitamin D deficiency, unspecified）後重新評估，本次建議為 **Hold**。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（VDDR Type 1B 亞型）**

**理由：**
維生素D依賴性佝僂病 Type 1B（CYP2R1突變，25-羥化酶缺陷）是 calcifediol 機轉匹配度最精準的孤兒藥適應症，直接替代患者無法自行合成的代謝中間物，理論上具有根治性潛力；現有文獻（L3）已清楚描述疾病機轉，但針對 calcifediol 的前瞻性干預試驗仍付之闕如，需在嚴格亞型分層下方可推進。

**若要推進需要：**
- 補充 calcifediol 詳細作用機轉資料（DrugBank MOA）
- 補充香港 / 台灣藥監局仿單警語與禁忌（安全性初評所需）
- 進行 VDDR 亞型精確基因分型（CYP2R1 vs CYP27B1 vs VDR 突變），以確定 calcifediol 有效的目標族群
- 評估 VDDR-1B 孤兒藥資格認定的可行性（全球僅報告少數家族）
- 設計以 CYP2R1 突變患者為入組條件的前瞻性小型試驗或擴展性療法（Expanded Access）方案
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

