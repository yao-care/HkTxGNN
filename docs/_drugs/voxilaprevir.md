---
layout: default
title: Voxilaprevir
parent: 僅模型預測 (L5)
nav_order: 802
evidence_level: L5
indication_count: 5
---

# Voxilaprevir
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

# Voxilaprevir：從C型肝炎病毒感染到B型肝炎病毒感染

## 一句話總結

Voxilaprevir 是 NS3/4A 蛋白酶抑制劑，依 Evidence Pack 中收集到的臨床試驗研判，其原本用途應為慢性C型肝炎病毒（HCV）感染治療（三合一複方 sofosbuvir/velpatasvir/voxilaprevir，商品名 Vosevi 的成分之一），但此正式適應症資訊在資料庫中缺失（Data Gap）。TxGNN 模型預測它可能對**B型肝炎病毒感染 (Hepatitis B Virus Infection)** 有效，預測分數高達 **99.84%**，但目前收集到的 **5 個臨床試驗**與 **10 篇文獻**經逐筆檢視後，全部研究對象皆為C型肝炎，並無任何一筆直接針對B型肝炎驗證療效，證據基礎薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 官方適應症資料缺失（Data Gap, DG002）；依臨床試驗證據推斷應為慢性C型肝炎病毒感染合併療法成分 |
| 預測新適應症 | B型肝炎病毒感染 (Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5（雖有多個已完成 Phase 3/4 試驗，但全數針對C型肝炎，並非針對此預測適應症，故不能採計為直接證據） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Data Gap, DG002）。根據 Evidence Pack 中收集到的臨床試驗佐證，Voxilaprevir 應是 sofosbuvir/velpatasvir/voxilaprevir 三合一複方（商品名 Vosevi）的成分之一，臨床角色是 NS3/4A 蛋白酶抑制劑，用於治療慢性C型肝炎病毒（HCV）感染，特別是先前接受直接抗病毒藥物（DAA）治療失敗的病人（見 NCT04695769、NCT06180590、NCT05092074 等多項 Phase 3/4 試驗）。

C型肝炎與B型肝炎雖同屬「病毒性肝炎」大類，且皆以肝臟為主要受累器官，但兩者病毒學上差異極大：HCV 屬 *Flaviviridae* 科 *Hepacivirus* 屬，為單股正鏈 RNA 病毒，其生命週期依賴 NS3/4A 蛋白酶進行聚蛋白裂解，這正是 Voxilaprevir 的藥理標的；而B型肝炎病毒（HBV）屬 *Hepadnaviridae* 科，為具反轉錄酶活性的部分雙股 DNA 病毒，其複製機制與 HCV 完全不同，並不依賴 NS3/4A 類蛋白酶。

因此，TxGNN 給出的高分預測，較可能反映知識圖譜中「病毒性肝炎」疾病本體（disease ontology）上的鄰近關係，而非真正的藥理機轉同源性。這也與 Evidence Pack 中另兩個排序較低的預測適應症（動物病毒性肝炎、Omsk 出血熱）已標註的評分結果一致——後兩者的證據等級同樣被判定為 L5、建議 Hold，理由也明確指出「僅為知識圖譜評分」「缺乏交叉活性數據」。B型肝炎的預測雖然分數更高，但同樣面臨機轉上缺乏支持、且無任何直接測試證據的問題。

---

## 臨床試驗證據

以下 5 筆試驗為 Evidence Pack 針對「B型肝炎病毒感染」預測所檢索到的相關試驗，**但需特別注意：全部試驗的實際研究對象皆為C型肝炎（HCV）患者，並非B型肝炎**，僅供了解藥物本身的臨床發展脈絡參考：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | 已完成 | 87 | HIV／HCV共感染患者，評估HCV根除後心血管風險變化（非B型肝炎試驗） |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | 已完成 | 281 | Ribavirin併用SOF/VEL/VOX用於慢性HCV治療失敗患者之再治療（非B型肝炎試驗） |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | 招募中 | 200 | Vosevi用於DAA治療失敗HCV患者之前瞻性世代研究（非B型肝炎試驗） |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | 已完成 | 15 | 比較二合一（SOF/VEL）與三合一（SOF/VEL/VOX）DAA對HCV病毒動力學及肝臟之影響（非B型肝炎試驗） |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | 已完成 | 15 | 評估SOF/VEL/VOX與荷爾蒙避孕藥（諾孕酯/炔雌醇）之藥物交互作用（非B型肝炎試驗） |

**結論：目前無任何一筆臨床試驗實際針對B型肝炎病毒感染測試 Voxilaprevir 之療效。**

---

## 文獻證據

以下文獻同樣是 Evidence Pack 針對此預測適應症所檢索到的相關文獻，**但主題絕大多數仍圍繞C型肝炎，並非B型肝炎的直接治療證據**：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | 單臂臨床試驗 | Lancet Gastroenterol Hepatol | 盧安達SHARED-3試驗：SOF/VEL/VOX用於HCV基因型4非a/d亞型DAA治療失敗患者之再治療（非B肝） |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | 真實世界研究 | J Gastrointestin Liver Dis | 羅馬尼亞真實世界資料：SOF/VEL/VOX治療HCV基因型1b、DAA失敗患者之療效與安全性（非B肝） |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | 世代研究 | J Clin Exp Hepatol | 印度HCV消除計畫中，DAA治療失敗相關抗藥性突變與預測因子分析（非B肝） |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | 回顧文獻 | Semin Liver Dis | DAA治療失敗後HCV患者之再治療策略回顧（非B肝） |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | 回顧文獻 | Clin Pharmacokinet | C型肝炎治療藥物藥動學／藥效學回顧2019更新（非B肝） |
| [31915372](https://pubmed.ncbi.nlm.nih.gov/31915372/) | 2020 | 回顧文獻 | Nat Rev Gastroenterol Hepatol | 病毒血症器官移植與抗病毒治療新方法（摘要未提供，非B肝專論） |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | 基礎研究 | Hepatology | HCV蛋白酶抑制劑抗藥性逃逸突變株之演化路徑與持續機制研究（非B肝） |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | 會議報告 | AIDS Rev | 2017國際病毒性肝炎大會報告，涵蓋HBV與HCV治療進展及全球消除目標 |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | 橫斷性研究 | Ann Hepatol | 比較美國與其他高所得國家B型與C型肝炎抗病毒藥物之定價差異（藥物經濟學，非療效證據） |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | 流行病學研究 | Vopr Virusol | 牙科患者中HIV/HBV/HCV血源性感染標記盛行率與病毒株系統發生分析（非治療性證據） |

**結論：僅第29369303篇（會議報告）與第40414600篇（藥價比較）涉及HBV，但均非療效或安全性研究，無法作為Voxilaprevir治療B型肝炎的實證支持。**

---

## 香港上市資訊

本藥物目前於香港**未上市**，無任何許可證登記（`total_licenses = 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（補充說明：Evidence Pack 標記「TFDA仿單警語/禁忌」為 **Blocking** 等級資料缺口，直接導致本案無法進入 S1 安全性初評階段。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 預測分數雖高（99.84%），但逐筆檢視所有檢索到的臨床試驗與文獻後，發現全部證據實際針對藥物既有適應症（C型肝炎），**沒有任何一筆直接研究 Voxilaprevir 於B型肝炎的療效**；HCV（RNA病毒，依賴NS3/4A蛋白酶）與HBV（DNA病毒，反轉錄酶依賴）在病毒學與藥理標的上差異顯著，機轉合理性存疑。
- 藥物作用機轉（MOA）與安全性資料（警語、禁忌症）均為 Blocking 等級的資料缺口，安全性初評（S1）目前無法進行。
- 香港未上市、無許可證登記，缺乏在地法規基礎。

**若要推進需要：**
- 補齊 DrugBank MOA 資料（DG002），釐清 Voxilaprevir 對HBV是否有任何理論或體外活性基礎。
- 取得 TFDA／香港衛生署仿單警語與禁忌症資料，完成 S1 安全性初評（DG001，Blocking）。
- 針對性搜尋是否存在 Voxilaprevir 或同類 NS3/4A 蛋白酶抑制劑於 HBV 動物模型或體外抗病毒活性之研究。
- 若無法找到機轉或臨床層級的直接支持證據，建議將此預測標記為低優先候選，資源優先投入證據較充分的其他候選藥物。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

